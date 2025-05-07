#!/bin/bash

echo "=== Starting Remote Workers ==="
srun --mail-type=END,FAIL --mail-user=YOUR_EMAIL_ADDRESS_HERE python3 taskReport.py
echo "=== Done ==="
