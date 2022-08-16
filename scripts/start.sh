#!/usr/bin/env bash

# Set working directory
DIR=$(cd -P -- "$(dirname -- "$0")" && echo "$(pwd -P)/..")

cd $DIR
source venv/bin/activate
python vocalize.py
