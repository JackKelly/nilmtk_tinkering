from __future__ import print_function, division
from nilmtk import DataSet, TimeFrame, MeterGroup
from nilmtk.utils import capitalise_index, capitalise_legend
import pandas as pd

# Plotting
def _mm_to_inches(*mms):
    return [mm / 25.4 for mm in mms]

%matplotlib qt 
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="white")
from pylab import rcParams
rcParams['figure.figsize'] = _mm_to_inches(180, 100) # 180 or 88mm wide for Scientific Data

dataset = DataSet('/data/mine/vadeec/merged/ukdale.h5')
TZ = dataset.metadata['timezone']
elec = dataset.buildings[1].elec

for building in dataset.buildings.values():
    try:
        building.elec.use_alternative_mains()
    except RuntimeError:
        pass
    else:
        print("using alternative mains for", building)

window_per_house = {1: ("2013-04-12", None), 
                    2: ("2013-05-22", None), 
                    3: (None, None), 
                    4: (None, None), 
                    5: (None, "2014-09-06")}
descriptions = []
for house in range(1,6):
    print("*********** House", house, "*************")
    dataset.set_window(*window_per_house[house])
    description = elec.describe()
    descriptions.append(description)
    print(description)
    print()