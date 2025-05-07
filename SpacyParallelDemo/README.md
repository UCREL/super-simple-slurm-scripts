# SpacyParallelDemo

This demo uses the python `spacy` package to process a bunch of text on independent workers.

To run this demo, first create a virtual environment with `python3 -m venv venv` and activate it with `source venv/bin/activate`.

Once this is done you can install the required libraries with `pip install -r requirements.txt` and install the required spacy model with `python -m spacy download en_core_web_sm`