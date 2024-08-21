#!/usr/bin/env bash

MODEL_FILE=kaldi_model_daanzu_20211030-biglm.zip

wget https://github.com/daanzu/kaldi-active-grammar/releases/download/v3.1.0/$MODEL_FILE
unzip $MODEL_FILE
rm -rf $MODEL_FILE
