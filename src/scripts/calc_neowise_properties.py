import numpy as np
import matplotlib.pyplot as plt
from astropy.io import ascii
from astropy.time import Time
import paths

twi = ascii.read(paths.data / 'obs_NEOWISE.ecsv')

# calculate mean fluxes before and after the event

t_mid = 58150
m_before = (twi['MJD']<t_mid)
t_before = np.max(twi['MJD'][m_before])
t_after = np.min(twi['MJD'][~m_before])

date_before = Time(t_before, format='mjd')
date_after = Time(t_after, format='mjd')

t_dur = t_before - t_after
date_bef = date_before.to_value(format='iso', subfmt='date')
date_aft = date_after.to_value(format='iso', subfmt='date')

coll_str = f'The increase in NEOWISE flux occurred between MJD {t_before:5.2f} (UT {date_bef}) and MJD {t_after:5.2f} (UT {date_aft}).'
with open(paths.output / 'collision_epoch_text.txt', 'w') as f:
    f.write(coll_str)

with open(paths.output / 'collision_epochs.txt', 'w') as f:
    f.write(f'{t_before:5.2f} {t_after:5.2f}')

with open(paths.output / 't_before.txt', 'w') as f:
    f.write(f'{t_before:5.2f}')
with open(paths.output / 't_after.txt', 'w') as f:
    f.write(f'{t_after:5.2f}')
with open(paths.output / 't_duration.txt', 'w') as f:
    f.write(f'{t_dur:5.1f}')
