# -*- coding: utf-8 -*-


# Load the Data
import pandas as pd

df = pd.read_csv(r"C:/Users/RISHI YADAV/Desktop/Project -01/Copy of pallet_Masked_fulldata.csv")

import sweetviz as sv

s = sv.analyze(df)
s.show_html()


# Autoviz
###########

from autoviz.AutoViz_Class import AutoViz_Class

av = AutoViz_Class()
a = av.AutoViz(r"D:/Data/education.csv", chart_format = 'html')

import os
os.getcwd()

# If the dependent variable is known:
a = av.AutoViz(r"C:/Data/education.csv", depVar = 'gmat') 



# D-Tale
########


import dtale
import pandas as pd

df

d = dtale.show(df)
d.open_browser()


# Pandas Profiling
###################

pip install pandas_profiling
from pandas_profiling import ProfileReport 

p = ProfileReport(df)
p
p.to_file("output.html")

import os
os.getcwd()

# Dataprep
##########

# pip install dataprep
from dataprep.eda import create_report

report = create_report(df, title = 'My Report')

report.show_browser()


