# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 16:30:56 2025

@author: SOMIKA ARYA
"""

import pandas as pd
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly_white"

data = pd.read_csv("Instagram-Reach.csv", encoding = 'latin-1')
print(data.head())
