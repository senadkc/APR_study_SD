# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 21:46:01 2025

@author: sena
"""

import sys
import os
from pathlib import Path
from shutil import copyfile

def find_standard_tokenize():
    """Find the location of Python's standard tokenize.py file."""
    for path in sys.path:
        tokenize_path = Path(path) / "tokenize.py"
        if tokenize_path.exists():
            return tokenize_path
    return None

def replace_standard_tokenize(custom_tokenize_path):
    """Replace the standard tokenize.py with the custom one."""
    standard_tokenize = find_standard_tokenize()

    if not standard_tokenize:
        print("Error: Could not find standard tokenize.py.")
        return
    
    # Backup the original tokenize.py before replacing
    backup_file = standard_tokenize.with_suffix(".bak")
    if not backup_file.exists():
        copyfile(standard_tokenize, backup_file)
        print(f"Backup created: {backup_file}")

    # Replace the standard tokenize.py with the custom version
    copyfile(custom_tokenize_path, standard_tokenize)
    print(f"Replaced {standard_tokenize} with {custom_tokenize_path}")

if __name__ == "__main__":
    # Get the custom tokenize.py file from the same folder as this script
    custom_tokenize = Path(__file__).parent / "tokenize.py"

    if not custom_tokenize.exists():
        print("Error: No tokenize.py found in the current directory!")
    else:
        replace_standard_tokenize(custom_tokenize)
