#!/usr/bin/env bash

export FLASK_APP=main.py

flask run --host=0.0.0.0 2>&1 | tee "logs/website_runtime_`date +%m-%d-%y_%H-%M-%S`.log"
