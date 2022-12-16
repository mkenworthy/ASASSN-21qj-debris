import numpy as np
import matplotlib.pyplot as plt
import pickle
import utils

import paths

# relevant parameters from SED fit
# WISE precision + photosphere precision
# ALMA flux limit
f_lim = [0.00085072, 0.00006   ]
lim_wav = [4.6, 880]
distance = 567.2
lstar = 1.
r_disk_bb = 0.089

r2t = lambda r: 278.3/np.sqrt(r) * lstar**0.25
t2r = lambda t: (278.3/t)**2 * lstar**2

# some arrays
r = np.logspace(-2, 2)
temp = r2t(r)

lims = [] #np.array([])
for i,_ in enumerate(f_lim):
    lim = 3.4e9 * f_lim[i] * distance**2 / r**2 / utils.bnu_wav_micron(lim_wav[i],temp)
    lims.append(lim)
    
lims = np.array(lims)

f = 0.034 # fractional luminosity from SED fit

# estimate emitting dust area from L = sigma_k A T^4
# and in Solar radii with A = 4pi R^2
sigma_k = 5.67e-8
Lsun = 3.83e26
Rsun = 6e8
tdust = 1000

area = f * lstar * Lsun / (sigma_k * tdust**4)
print(area / 1.5e11**2)
np.sqrt(area / 4 / np.pi) / Rsun

fig, ax = plt.subplots(figsize=(5.8,4))

ax.vlines(1, *ax.get_ylim(), linestyles=':', label='Optical duration')
ax.vlines(36, *ax.get_ylim(), linestyles='-.', label='Optical gradients')
ax.vlines(2, *ax.get_ylim(), linestyles='--', label='IR-opt delay')

ok = r > r_disk_bb
ax.loglog(r[ok], lims[0,ok]*4.2, 'red', label='WISE W2 flux')
ax.loglog(r[ok], lims[1,ok],label='ALMA upper limit')

ax.plot(r_disk_bb, f, 'or')

ax.loglog(r, lims[0], 'grey', alpha=0.5, label='WISE limit')

secax = ax.secondary_xaxis('top', functions=(r2t, t2r))
secax.set_xlabel('temperature / K')

ax.set_ylim(2e-3,1)
ax.set_xlim(1e-2,1e2)
ax.set_xlabel('radius / au')
ax.set_ylabel('fractional luminosity')
ax.legend()

fig.savefig(paths.figures / 'fvsr.pdf')
