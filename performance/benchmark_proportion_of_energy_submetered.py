from __future__ import print_function, division
from nilmtk import DataSet, TimeFrame
from time import time
import pandas as pd

TZ = 'Europe/London'

ukdale = DataSet('/data/mine/vadeec/merged/ukdale.h5')
ukdale.store.window = TimeFrame(start=pd.Timestamp('2014-10-20 06:24:33', tz=TZ),
                                end=pd.Timestamp('2014-10-27 06:24:33', tz=TZ))
# ukdale.store.window = TimeFrame(start='2014-10-20 06:24:33+0100', 
#                                 end='2014-10-27 06:24:33+0000')

elec = ukdale.buildings[1].elec
elec.use_alternative_mains()
elec.clear_cache()

t0 = time()
proportion = elec.proportion_of_energy_submetered()
t1 = time()

print("Proportion =", proportion)
print("Time =", t1 - t0)
print("----------------------------------------------")

t0 = time()
proportion = elec.proportion_of_energy_submetered()
t1 = time()

print("Proportion =", proportion)
print("Time =", t1 - t0)

