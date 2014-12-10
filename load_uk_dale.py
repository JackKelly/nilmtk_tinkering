from nilmtk import DataSet

ukdale = DataSet('/data/mine/vadeec/merged/ukdale.h5')
elec = ukdale.buildings[1].elec
elec.use_alternative_mains()
