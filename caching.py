from __future__ import print_function, division
from nilmtk import DataSet

ukdale = DataSet('/data/mine/vadeec/merged/ukdale.h5')
elec = ukdale.buildings[1].elec
meter = elec[1]

# total_energy_dict = {
#     'timeframes': [meter.get_timeframe().to_dict()],
#     'total_energy': {'apparent': meter.total_energy()}
# }
# meter.metadata['statistics'] = [total_energy_dict]

print(meter.get_stat_from_metadata('total_energy'))
