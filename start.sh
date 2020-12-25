#!/bin/bash

# exec python encrypter.py
# exec python test.py
python sample.py

# pyinstaller test.py --key hogepiyofuga

pyinstaller sample.py --clean --onefile 