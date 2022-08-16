#!/usr/bin/env bash

./download-model.sh
python -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
