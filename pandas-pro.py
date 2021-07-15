import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport
import os
import random

from os import listdir
from os.path import isfile, join

CSV_PATH = "csv"
FILES = [f for f in listdir(CSV_PATH) if isfile(join(CSV_PATH, f))]


def generate_pandas_profile(filename):
    df = pd.read_csv("csv/{}".format(filename))

    print("Generating pandas profile report for file: {}".format(filename))
    # Run standard profile report
    profile = ProfileReport(
        df,
        title="{}".format(filename),
        html={"style": {"full_width": True}},
        minimal=True,
    )

    # Saving as HTML File
    profile.to_file(
        output_file="output/html/{}.html".format(filename[:-4])
    )  # pop .csv from string

    # As a file
    profile.to_file(
        output_file="output/json/{}.json".format(filename[:-4])
    )  # pop .csv from string

    print("SUCCESS! Pandas profile report created for file: {}".format(filename))


def main():
    for file in FILES:
        generate_pandas_profile(file)


if __name__ == "__main__":
    main()
