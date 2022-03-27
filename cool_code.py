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
import requests, zipfile, io  # for file download, extract

dataset = "OnlineNewsPopularity"

# =============================================================================
# get data
# =============================================================================

# OS and directory agnostic pointer to top level directory
dir_top = os.path.dirname(__file__)
dir_top = os.path.join(dir_top, "data", "input")

# point to destination directory
dir_dest = os.path.join(dir_top, dataset)

# point to destination file
filepath = os.path.join(dir_dest, dataset + ".csv")

# avoid unnecessary downloading and extracting the file each run
if not os.path.isfile(filepath):
    print("Data file does not exist on local. Downloading...")

    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00332/"

    # download and extract
    res = requests.get(url + dataset + ".zip")
    z = zipfile.ZipFile(io.BytesIO(res.content))
    z.extractall(dir_top)

df = pd.read_csv(filepath)

# %%

# =============================================================================
# cool stuff
# =============================================================================

