#!/usr/bin/env bash

# Set working directory
DIR=$(cd -P -- "$(dirname -- "$0")" && echo "$(pwd -P)/..")
cd $DIR

# Activate virtual environment
CONDA_BASE=$(conda info --base)
source $CONDA_BASE/etc/profile.d/conda.sh
conda activate vocalize

# Run vocalize
python vocalize.py
