import numpy as np
import matplotlib.pyplot as plt
from astropy.io import ascii
from astropy.time import Time
from astropy.timeseries import LombScargle

import paths

import matplotlib as mpl
mpl.rcParams.update({'font.size': 14})

twi = ascii.read(paths.data / 'obs_NEOWISE.ecsv')
tat = ascii.read(paths.data / 'obs_ATLAS.ecsv')
tas = ascii.read(paths.data / 'obs_ASASSN.ecsv')

tasg = tas[tas['Filter']=='g']
tasV = tas[tas['Filter']=='V']

# calculating Lomb scargle over quiet photometry of V filter including two quiet years
t_quiet_start = 57600.
t_quiet_end   = 58131.

# select quiet star photometry
m = (tasV['MJD']>t_quiet_start) * (tasV['MJD']<t_quiet_end)

tasVm=tasV[m]
frequency, power = LombScargle(tasV['MJD'], tasV['fnorm']-1.0,tasV['fnormerr']).autopower()

frequencym, powerm = LombScargle(tasVm['MJD'], tasVm['fnorm']-1.0,tasVm['fnormerr']).autopower()

t_ecli_start = 59314.
t_ecli_end   = 59750.


# select quiet star photometry
m2 = (tasg['MJD']>t_ecli_start) * (tasg['MJD']<t_ecli_end)

tasgecl=tasg[m2]

frequencym2, powerm2 = LombScargle(tasgecl['MJD'], tasgecl['fnorm']-1.0,tasgecl['fnormerr']).autopower()



fig, (ax1,ax2,ax3) = plt.subplots(3,1,figsize = (10,7))


ax1.scatter(tasg['MJD'],tasg['fnorm'],
    color='green',
    alpha=0.2,
    s=10,
    edgecolors='none',
    label='ASASSN g\'')
ax1.scatter(tasV['MJD'],tasV['fnorm'],
    color='blue',
    alpha=0.2,
    s=10,
    edgecolors='none',
    label='ASASSN V')

ax1.axvspan(t_quiet_start, t_quiet_end, alpha=0.2, color='blue')
ax1.axvspan(t_ecli_start, t_ecli_end, alpha=0.2, color='orange')


ax2.plot(1./frequencym, powerm, color='blue')
ax2.plot(1/frequencym2, powerm2, color='orange')
#ax3.set_ylim(0,1.1)
ax2.set_xlim(0,150)
#ax3.set_xlim(0,50)
ax3.plot(1./frequencym, powerm, color='blue')
ax3.set_xlim(0,50)

ax1.set_ylim(0,1.1)
ax1.set_xlim(56600,59800)
ax1.legend()
ax1.set_xlabel('Epoch [MJD]')
ax2.set_xlabel('Period [days]')
ax3.set_xlabel('Period [days]')

ax1.set_ylabel('Normalised flux')
ax2.set_ylabel('Power')
ax3.set_ylabel('Power')

plt.savefig(paths.figures / 'stellar_lomb_scargle.pdf',
    bbox_inches='tight',
    dpi=200)
plt.draw()
plt.show()
