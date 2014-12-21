from __future__ import print_function, division
from nilmtk import DataSet, TimeFrame
from nilmtk.elecmeter import ElecMeterID
import pandas as pd

ukdale = DataSet('/data/mine/vadeec/merged/ukdale.h5')
# TZ = 'Europe/London'
# ukdale.store.window = TimeFrame(pd.Timestamp("2014-01-01 00:00", tz=TZ),
#                                 pd.Timestamp("2014-01-02 00:00", tz=TZ))

ukdale.set_window("2013-04-01", "2013-05-01")

elec = ukdale.buildings[1].elec
meter = elec[2]
# ukdale.plot_good_sections()

# best = meter._convert_physical_quantity_and_ac_type_to_cols(ac_type='best')
# elec2 = ukdale.buildings[2].elec
# elec.use_alternative_mains()
# elec2.use_alternative_mains()
# submeters2 = elec2.submeters()

# gen = submeters2.load()
# df = next(gen)

# gen = elec.load(verbose=True) 
# df = gen.next()
# corr = elec.correlation_of_sum_of_submeters_with_mains(verbose=True)

# prop = elec.proportion_of_energy_submetered()

# submeters = elec.meters_directly_downstream_of_mains()
# grouped = submeters.groupby('type')
# top_k = grouped.select_top_k(group_remainder=True)

# top_k.plot(kind='area')
# lights = elec.meters_directly_downstream_of_mains().select_using_appliances(type='light')
# lights.sort_meters()

# ukdale.clear_cache()
# ukdale.plot_good_sections()
# ukdale.plot_histograms_of_mains_power()
