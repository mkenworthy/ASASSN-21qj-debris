import numpy as np
import matplotlib.pyplot as plt
from astropy.io import ascii
import paths


#twi = ascii.read(paths.data / 'obs_NEOWISE.ecsv')
tat = ascii.read(paths.data / 'obs_ATLAS.ecsv')
tas = ascii.read(paths.data / 'obs_ASASSN.ecsv')
tav = ascii.read(paths.data / 'obs_AAVSO.ecsv')

print('running plot_eclipse_overview2.py...')

tat_by_filter = tat.group_by('Filter')
print('ATLAS all observed photometric bands:')
print(tat_by_filter.groups.keys)

tas_by_filter = tas.group_by('Filter')
print('ASASSN all observed photometric bands:')
print(tas_by_filter.groups.keys)

tav_by_filter = tav.group_by('Filter')
print('AAVSO all observed photometric bands:')
print(tav_by_filter.groups.keys)

fig, (ax1) = plt.subplots(1,1,figsize = (16,6))

# order should be....
tavB = tav[tav['Filter']=='B']
tasg = tas[tas['Filter']=='g']
tatc = tat[tat['Filter']=='c']
tasV = tas[tas['Filter']=='V']
tavV = tav[tav['Filter']=='V']
tato = tat[tat['Filter']=='o']
tavI = tav[tav['Filter']=='I']
offset = 0.6

ax1.errorbar(tavB['MJD'],tavB['fnorm']+3*offset,yerr=tavB['fnormerr'],color='green',fmt='.', label='AAVSO B')
ax1.errorbar(tasg['MJD'],tasg['fnorm']+2*offset,yerr=tasg['fnormerr'],color='orange',fmt='.', label='ASASSN g\'')
#ax1.errorbar(tatc['MJD'],tatc['fnorm']+4*offset,yerr=tatc['fnormerr'],color='green',fmt='.', label='')
#ax1.errorbar(tasV['MJD'],tasV['fnorm']+2*offset,yerr=tasV['fnormerr'],color='yellow',fmt='.', label='')
ax1.errorbar(tavV['MJD'],tavV['fnorm']+1*offset,yerr=tavV['fnormerr'],color='red',fmt='.', label='AAVSO V')
#ax1.errorbar(tato['MJD'],tato['fnorm']+1*offset,yerr=tato['fnormerr'],color='red',fmt='.', label='')
ax1.errorbar(tavI['MJD'],tavI['fnorm']+0*offset,yerr=tavI['fnormerr'],color='brown',fmt='.', label='AAVSO I')

ax1.set_ylim(0,3.1)
ax1.set_xlim(59300,60000)
ax1.legend()
ax1.set_xlabel('Epoch [MJD]',fontsize=18)
ax1.tick_params(axis='x', labelsize=12)
ax1.tick_params(axis='y', labelsize=12)
ax1.set_ylabel('Normalised flux plus offset',fontsize=18)
ax1.hlines(np.arange(8)*offset+1,59000,60000,color='grey',alpha=0.5)
ax1.vlines(np.arange(59300,60000,50),0,5,color='grey',alpha=0.5)


plt.savefig(paths.figures / 'eclipse_overview2.pdf', bbox_inches='tight')
plt.show()
