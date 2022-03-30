# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 21:41:15 2022

@author: cool dudez

  ___  ____  __  __  __  __  ____       ____    __   ____   __   
 / __)(_  _)(  \/  )(  \/  )( ___)     (  _ \  /__\ (_  _) /__\  
( (_-. _)(_  )    (  )    (  )__)  ___  )(_) )/(__)\  )(  /(__)\ 
 \gm_/(____)(_/\/\_)(_/\/\_)(____)(___)(____/(__)(__)(__)(__)(wk)

The design decision was to to not turn this into a function, since no other
DATASETs will likely match this particular structure.

IMPROVEMENTS:
Generalize this for other zip files.

"""

import os
import requests, zipfile, io  # for file download, extract

DATASET = "OnlineNewsPopularity"

# =============================================================================
# get data
# =============================================================================

# OS and directory agnostic pointer to top level directory
dir_py = os.path.dirname(__file__)
dir_top = os.path.join(dir_py, "data", "input")

# point to destination directory
dir_dest = os.path.join(dir_py, "data", "input", DATASET)
print(f"Data directory: {dir_dest}")

# point to destination file
filepath = os.path.join(dir_py, "data", "input", DATASET, DATASET + ".csv")

# avoid unnecessary downloading and extracting the file each run
if not os.path.isfile(filepath):
    print("Data file does not exist locally. Downloading...")

    url = f"https://archive.ics.uci.edu/ml/machine-learning-databases/00332/{DATASET}.zip"

    # download and extract
    res = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(res.content))
    z.extractall(dir_top)

    print("Data downloaded from: {url}")
    print("Data downloaded to: {dir_dest}")
