# Vocalize

Voice control for macOS with a Vim mindset.

## Requirements

- python ^3.10.0
- virtualenv ^20.16.0

## Installation

1.  Download the Kaldi model

        ./scripts/download-model.sh

2.  Create a virtual environment

        python -m virtualenv venv

3.  Activate the virtual environment

        source venv/bin/activate

4.  Install the project dependencies

        pip install -r requirements.txt

## Getting Started

1.  Activate the virtual environment (if you haven't done so already)

        source venv/bin/activate

2.  Run vocalize

        python vocalize.py

## Deactivating the Virtual Environment

    deactivate

## Keybindings

This project assumes you have the following keybindings configured:

- Dictation: Control + Shift + D
