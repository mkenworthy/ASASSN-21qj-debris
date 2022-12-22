import numpy as np
from astropy import constants as c
from astropy import units as u

from asassn21qj import *

v_tran = 5.0*u.km/u.s
v_exp  = 1.0*u.km/u.s
t_eclipse = 400*u.day

print(f'Transverse velocity is {v_tran:4.2f}')
print(f'Expansion velocity is {v_exp:4.2f}')
print(f'Duration of the eclipse {t_eclipse:4.0f}')
total_length = (v_tran*t_eclipse).to(u.au)
print(f'Length of strip is {total_length:4.2e}')

total_strip_area = (v_tran*t_eclipse * 2*star_rad).to((u.cm*u.cm))
print(f'area of the strip is {total_strip_area:4.2e}')

r_dust = 0.1 * u.micron

rho_dust = 3.0 * u.gram / (u.cm*u.cm*u.cm)

area_dust = np.pi * r_dust * r_dust # area of 1 particle

mass_dust = (4./3.) * np.pi * r_dust * r_dust * r_dust # mass of 1 particle

total_mass_strip = (rho_dust * total_strip_area * mass_dust / area_dust).to(u.gram)



print(f'total mass of strip is {total_mass_strip.to(u.Mearth):4.2e}')
print(f'total mass of strip is {total_mass_strip.to(u.gram):4.2e}')

print('if we assume that the expansion is isotropic from the collision, we can estimate the total mass of the eclipsing shell by assuming it has expanded as a perfect sphere of diameter of the strip.')

total_area_disk = np.pi*np.power(v_tran*t_eclipse/2, 2) 

disk_aspect = 0.3
total_mass_disk = (disk_aspect * rho_dust * total_area_disk * mass_dust / area_dust).to(u.gram)



print(f'total mass of disk with aspect {disk_aspect} is {total_mass_disk.to(u.Mearth):4.2e}')
print(f'total mass of disk with aspect {disk_aspect} is {total_mass_disk.to(u.gram):4.2e}')

