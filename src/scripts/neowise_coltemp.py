import numpy as np
from astropy.table import Table
import paths
from utils import col2temp

# read from csv created by convert_neowise
t = Table.read(paths.data/'obs_NEOWISE.ecsv')

# get photospheric flux and subtract to get dust colour
# we assume that pre-increase was just the star (which
# may include the companion, it doesn't matter)
w1flux = 302.878 * 10**(-0.4*t['w1'])
w2flux = 172.415 * 10**(-0.4*t['w2'])
ok = t['MJD'] < 58100
w1phot = np.median(w1flux[ok])
w2phot = np.median(w2flux[ok])
w1xs = w1flux - w1phot
w2xs = w2flux - w2phot

# now get colour temp, floats are the mean wavelengths
# for the WISE W1 and W2 bands
w1w2temp = []
for i in range(len(t['MJD'])):
    w1w2temp.append(col2temp([3.3791878170787886, 4.629290939920992],
                             [w1xs[i], w2xs[i]])
                   )
tout = Table([t['MJD'], w1xs, w2xs, w1w2temp],
             names=['MJD','w1excess','w2excess','w1w2temp'])

tout.write(paths.data/'NEOWISE_coltemp.ecsv',format='ascii.ecsv',overwrite=True)
