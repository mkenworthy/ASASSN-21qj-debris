import numpy as np
from astropy import constants as c
from astropy import units as u
from astropy.io import ascii
import matplotlib.pyplot as plt

import paths

from asassn21qj import *


def dxdtmin (ldot,rstar): # equation 12 from van Werkhoeven 2014 MNRAS 441 2845
    vmin = 13 * (u.km/u.s) * ldot * rstar / (1.13 * u.Rsun)
    return vmin.to(u.km/u.s) # km/s


t = ascii.read(paths.data / 'asassn/light_curve_f51db35b-11b8-4840-a6d9-979a455d6978.csv')

# just look at the g band

tg = t[(t['Filter']=='g') * (t['flux_err'] < 0.5)]

mjd = tg['HJD']-2400000.5

fi, ax = plt.subplots(1,1,figsize=(8,4))

ax.errorbar(mjd, tg['flux(mJy)'],yerr=tg['flux_err'],fmt='.')

ax.set_xlabel('Epoch [MJD]')
ax.set_ylabel('Flux [mJy]')
ax.set_title('ASAS-SN g band photometry of J0815')

# by eye... forgive me for I know not what I have done.

t1 = 59672.63
f1 = 6.765
t2 = 59673.585
f2 = 4.807


ax.plot((t1,t2),(f1,f2),linewidth=3,zorder=10)

f_norm = 10.

df = (f1-f2)/f_norm
dt = t2-t1

dfdt = df/dt
tx = 'Rate of flux drop is {:.3f} $L_*/day$'.format(dfdt)
ax.text(0.8, 0.92, tx, ha='right',transform=ax.transAxes)

print(dxdtmin(dfdt,star_rad))
t4 = r'Minimum transverse velocity with 1.0$R_\odot$ is {:.2f}'.format(dxdtmin(dfdt,star_rad))

ax.text(0.8, 0.7, t4, ha='right',transform=ax.transAxes)

t1 = 59749.54
f1 = 8.56
t2 = 59751.65
f2 = 5.86

ax.plot((t1,t2),(f1,f2),linewidth=3,zorder=10)

f_norm = 10.

df = (f1-f2)/f_norm
dt = t2-t1

dfdt = df/dt
tx = 'Rate of flux drop is {:.3f} $L_*/day$'.format(dfdt)
ax.text(0.8, 0.6, tx, ha='right',transform=ax.transAxes)

print(dxdtmin(dfdt, star_rad))
t4 = r'Minimum transverse velocity with 1.0$R_\odot$ is {:.2f}'.format(dxdtmin(dfdt,star_rad))

ax.text(0.8, 0.5, t4, ha='right',transform=ax.transAxes)

ax.set_xlim(59400,59800)
ax.set_ylim(0,11)

plt.show()

v_tran = 2.4 * u.km / u.s
t_eclipse = 400 * u.day

total_strip = (v_tran * t_eclipse * 2 * star_rad).to((u.cm*u.cm))
print(f'area is {total_strip}')

r_dust = 0.1 * u.micron

rho_dust = 3.0 * u.gram / (u.cm*u.cm*u.cm)

area_dust = np.pi * r_dust * r_dust

mass_dust = (4./3.) * np.pi * r_dust * r_dust * r_dust

total_mass = (rho_dust * total_strip * mass_dust / area_dust).to(u.gram)

print(f'total mass of strip is {total_mass.to(u.Mearth)}')
