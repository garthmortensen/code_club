# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 21:47:33 2022

@author: cool dudez
                  ______              _________
_____________________  /  __________________  /____
_  ___/  __ \  __ \_  /   _  ___/  __ \  __  /_  _ \
/ /__ / /_/ / /_/ /  /    / /__ / /_/ / /_/ / /  gm/
\___/ \____/\____//_/     \___/ \____/\__,_/  \___/

"""

import os
import pandas as pd

# OS- and directory-agnostic pointer
filename = f"OnlineNewsPopularity.csv"
directory = os.path.dirname(__file__)
filepath = os.path.join(directory, "data", "input", filename)

df = pd.read_csv(filepath)
