from nilmtk import DataSet, TimeFrame
import pandas as pd

ukdale = DataSet('/data/mine/vadeec/merged/ukdale.h5')
# TZ = 'Europe/London'
# ukdale.store.window = TimeFrame(pd.Timestamp("2014-01-01 00:00", tz=TZ),
#                                 pd.Timestamp("2014-01-02 00:00", tz=TZ))

ukdale.set_window("2014-01-01", "2014-01-02")

elec = ukdale.buildings[1].elec
elec.use_alternative_mains()

# gen = elec.load(verbose=True) 
# df = gen.next()
# corr = elec.correlation_of_sum_of_submeters_with_mains(verbose=True)

prop = elec.proportion_of_energy_submetered()
