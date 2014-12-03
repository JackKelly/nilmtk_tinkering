"""This is a test for this issue that Nipun identified:
https://github.com/nilmtk/nilmtk/issues/265
"""

from __future__ import print_function, division
import nilmtk

we = nilmtk.DataSet('/data/wikienergy/wikienergy.h5')
nilmtk.global_meter_group.clear_cache()
fr = nilmtk.global_meter_group.select_using_appliances(building=11, type='fridge')
print(fr.proportion_of_upstream())
print("Now using cache...")
print(fr.proportion_of_upstream())

nilmtk.utils.show_versions()
