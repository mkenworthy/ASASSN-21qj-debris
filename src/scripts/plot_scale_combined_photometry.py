import numpy as np
import matplotlib.pyplot as plt
from astropy.io import ascii
import paths

print('running plot_scale_combined_photometry...')

tas = ascii.read(paths.data / 'obs_ASASSN.ecsv')
tav = ascii.read(paths.data / 'obs_AAVSO.ecsv')

tas_by_filter = tas.group_by('Filter')
print('ASASSN all observed photometric bands:')
print(tas_by_filter.groups.keys)

tav_by_filter = tav.group_by('Filter')
print('AAVSO all observed photometric bands:')
print(tav_by_filter.groups.keys)

fig, (ax1, ax2) = plt.subplots(2,1,figsize = (16,6),sharex=True)

# order should be....
tavB = tav[tav['Filter']=='B']
tasg = tas[tas['Filter']=='g']
tavV = tav[tav['Filter']=='V']
tavI = tav[tav['Filter']=='I']
offset = 0.6

#ax1.errorbar(tavB['MJD'],tavB['fnorm']+3*offset,yerr=tavB['fnormerr'],color='green',fmt='.', label='AAVSO B')
#ax1.errorbar(tasg['MJD'],tasg['fnorm']+2*offset,yerr=tasg['fnormerr'],color='orange',fmt='.', label='ASASSN g\'')
#ax1.errorbar(tavV['MJD'],tavV['fnorm']+1*offset,yerr=tavV['fnormerr'],color='red',fmt='.', label='AAVSO V')
#ax1.errorbar(tavI['MJD'],tavI['fnorm']+0*offset,yerr=tavI['fnormerr'],color='brown',fmt='.', label='AAVSO I')

ax2.set_xlim(59300,56000)
ax2.set_xlabel('Epoch [MJD]',fontsize=18)
ax2.tick_params(axis='x', labelsize=12)
ax2.tick_params(axis='y', labelsize=12)
fig.supylabel('Absorption',fontsize=18)
ax2.hlines(np.arange(8)*offset+1,59000,60000,color='grey',alpha=0.5)
ax2.vlines(np.arange(59300,60000,50),0,5,color='grey',alpha=0.5)

ax2.errorbar(tasg['MJD'],1.-tasg['fnorm'],yerr=tasg['fnormerr'],color='orange',
    alpha=0.5,
    fmt='.', label='ASASSN g\'')
ax2.errorbar(tavV['MJD'],(1.-tavV['fnorm']),yerr=tavV['fnormerr'],color='orange',
    alpha=0.5,
    fmt='.', label='AAVSO V')
ax2.errorbar(tavI['MJD'],(1.-tavI['fnorm']),yerr=tavI['fnormerr'],color='brown',
    alpha=0.5,
    fmt='.', label='AAVSO I')
ax2.errorbar(tavB['MJD'],(1.-tavB['fnorm']),yerr=tavB['fnormerr'],color='blue',
    alpha=0.5,
    fmt='.', label='AAVSO B')



ax1.scatter(tasg['MJD'],1.-tasg['fnorm'],color='black',
    alpha=0.5, edgecolors='none',
    s=10, label='ASASSN g\'')
ax1.scatter(tavV['MJD'],(1.-tavV['fnorm'])*1.1,color='black',
    alpha=0.5,edgecolors='none',
    s=10, label='AAVSO V')
ax1.scatter(tavI['MJD'],(1.-tavI['fnorm'])*2.0,color='black',
    alpha=0.5, edgecolors='none',
    s=10,label='AAVSO I')
ax1.scatter(tavB['MJD'],(1.-tavB['fnorm'])*0.85,color='black',
    alpha=0.5, edgecolors='none',
    s=10, label='AAVSO B')

ax1.set_ylim(0,1.26)
ax2.set_ylim(0,1.26)


plt.savefig(paths.figures / 'scale_combined_photometry.pdf', bbox_inches='tight')
#plt.show()
