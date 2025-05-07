#!/bin/bash
#SBATCH --partition=cpu-20c32g-5m
#SBATCH --output=log/output_%A_%a.log
#SBATCH --array=0-9

python3 spacyTag.py
