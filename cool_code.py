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
import requests, zipfile, io  # for donwloading file

filename = "OnlineNewsPopularity.csv"

# OS and directory agnostic pointer to top level directory
dir_top = os.path.dirname(__file__)
dir_top = os.path.join(dir_top,
                       "data",
                       "input")

# OS and directory agnostic pointer to destination directory
dir_dest = os.path.join(dir_top,
                        "OnlineNewsPopularity.csv",
                        "OnlineNewsPopularity")

# %%

for file in os.listdir(dir_dest):
    print(file)

# %%

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00332/"
filename = "OnlineNewsPopularity.zip"

res = requests.get(url + filename)
z = zipfile.ZipFile(io.BytesIO(res.content))
z.extractall(dir_top)

# %%

# df = pd.read_csv(filepath)
