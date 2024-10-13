# aps_cript

A simple hello world module

If you are going to *develop* from this repository, go to the [development guide](README_DEV.md).

## Installing aps_cript:

Remember to follow these instructions from within your preferred virtual environment:

    conda create -n aps_cript python=True
    conda activate aps_cript

The first way is to clone the repository and do a local installation:

    git clone https://github.com/isavrodrigues/aps_cript.git
    cd aps_cript
    pip install .

The second way is to install directly:

    pip install git+https://github.com/isavrodrigues/aps_cript.git

To uninstall, use:

    pip uninstall aps_cript

## Usage

To find all implemented commands, run:

    aps_cript-cli --help
