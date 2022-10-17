import numpy as np
import matplotlib.pyplot as plt
from astropy.io import ascii
from astropy.time import Time
import paths
from asassn21qj import *
from astropy import constants as c
from astropy import units as u
from kepler3 import *

f_IR = 0.03

a = np.logspace(-2,2,41) * u.au

v_circ = vcirc(star_mass, 1*u.Mjup, a)

fig, (ax1,ax2) = plt.subplots(2,1,figsize=(6,6), sharex=True)
ax1.loglog(a.to(u.au),v_circ.to(u.km/u.s))
ax1.set_ylabel('Circular velocity [km/s]')
ax2.set_ylabel('Dust eq temperature [K]')
ax2.set_xlabel('Distance from star [au]')
ax1.set_xlabel('Distance from star [au]')

AB=0.1
x = star_lum*(1-AB)/(16*c.sigma_sb*np.pi*a*a)
Teq = np.power(x,1./4).to(u.K)

gravpot = c.G*1.0*u.Mearth*1.0*u.Mearth/(1.0*u.Rearth)
print(f'Grav potential of 2 x 1Me masses is {gravpot.to(u.J):.1e}')
print(f'assuming {f_IR} fractional luminosity of star this results in a glow for {(gravpot/(f_IR*star_lum)).to(u.yr):5.3f}')
ax2.loglog(a.to(u.au),Teq)
plt.draw()
plt.show()
plt.savefig(paths.figures /'velocity_constraints.pdf',
    bbox_inches='tight')
