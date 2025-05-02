#!/bin/bash
#SBATCH --partition=cpu-20c32g-5m
#SBATCH --output=log/output_%A_%a.log
#SBATCH --array=0-7

python3 taskReport.py
