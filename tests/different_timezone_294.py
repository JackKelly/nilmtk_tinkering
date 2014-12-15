from __future__ import print_function, division

from nilmtk import DataSet
ds = DataSet("/data/mine/vadeec/merged/ukdale.h5")
elec = ds.buildings[1].elec
elec.load(chunksize=10).next()

# for meter in elec.meters:
#     print(meter)
#     print(meter.load(chunksize=10).next().index.tzinfo)
