# Vocalize

Voice control for your computer with a Vim mindset.

## Requirements

- python ^3.10.0
- virtualenv ^20.16.0

## Getting Started

1.  Download the Kaldi model

        ./scripts/download-model.sh

2.  Create a virtual environment

        python -m virtualenv venv

3.  Activate the virtual environment

        source venv/bin/activate

4.  Install the project dependencies

        pip install -r requirements.txt

5.  Run the demo

        python demo.py
