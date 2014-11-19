from __future__ import print_function, division
from nilmtk import DataSet, TimeFrame
from time import time

ukdale = DataSet('/data/mine/vadeec/merged/ukdale.h5')
ukdale.store.window = TimeFrame(start='2014-11-09 06:24:33.500000+01:00', 
                                end='2014-11-16 06:24:33.500000+00:00')
elec = ukdale.buildings[1].elec
#elec.meters = elec.meters[:-1]

t0 = time()
proportion = elec.proportion_of_energy_submetered()
t1 = time()

print("Proportion =", proportion)
print("Time =", t1 - t0)

