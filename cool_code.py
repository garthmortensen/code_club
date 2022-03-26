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

from pathlib import Path
import pandas as pd

filepath = Path("./data/input/OnlineNewsPopularity.csv")
df = pd.read_csv(filepath)

