import numpy as np
from astropy import constants as c
from astropy import units as u

from asassn21qj import *

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
