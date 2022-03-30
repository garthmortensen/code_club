# Code_Club

## Setup

To create the virtual environment and install required libraries, use commands:
```bash
python -m venv venv
source venv/Scripts/activate  # windows OS
source venv/bin/activate  # linux/mac OS
pip install -r requirments.txt
```

Or simply run `create_env.sh`:
```bash
./create_env.sh
```

## Data

We're pulling data from UCI Irvine Machine Learning Repositories, [here](https://archive-beta.ics.uci.edu/ml/datasets/online+news+popularity).

`cool_code.py` downloads and extracts the dataset on first run.

