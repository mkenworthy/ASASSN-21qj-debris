import numpy as np
import matplotlib.pyplot as plt
import paths
from specutils import Spectrum1D

from astropy import units as u

from astropy.visualization import quantity_support

quantity_support()
import matplotlib as mpl
mpl.rcParams.update({'font.size': 14})

spec = Spectrum1D.read(paths.data / '2spot/asassn-21qj_20220907_358_2SPOT.fits', format='wcs1d-fits')

fig, (ax1) = plt.subplots(1,1,figsize = (10,5))

ax1.plot(spec.wavelength, spec.flux,
    color='brown')

ax1.set_ylim(0,2)
##ax1.set_xlim(56600,59800)
#ax1.legend()
ax1.set_xlabel('Wavelength [Angstroms]')

plt.savefig(paths.figures / '2spot_spectrum.pdf',
    bbox_inches='tight',
    dpi=200)
plt.draw()
plt.show()
