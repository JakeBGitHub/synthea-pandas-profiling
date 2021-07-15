import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport
import os
import random


from os import listdir
from os.path import isfile, join

CSV_PATH = "csv"
FILES = [f for f in listdir(CSV_PATH) if isfile(join(CSV_PATH, f))]

# print(onlyfiles)


def sample_dataframe(df, filename, sample_size=50):

    n = len(df)
    st = os.stat('csv/{}'.format(filename))
    file_size = st.st_size

    sample_size = min(sample_size, n)
    skip = sorted(
        random.sample(range(1, n + 1), n - sample_size)
    )
    df = pd.read_csv('csv/{}'.format(filename), skiprows=skip)
    return df


# src_file = 'data/abc.csv'
# out_file = 'abc_profile.html'
# df , n , file_size =sample_dataframe(src_file, 99999)
# profile = df.profile_report()
# profile.to_file(output_file = out_file)


def generate_pandas_profile(filename):
    df = pd.read_csv("csv/{}".format(filename))

    # if (os.stat(filename )).st_size > 1000000:
    #     df = sample_dataframe(src_file, 99999)

    if len(df) > 40000:
        df = sample_dataframe(df, filename, 10000)


    print('Generating pandas profile report for file: {}'.format(filename))
    # Run standrd profile report
    profile = ProfileReport(
        df,
        title="Pandas Profiling Report",
        html={"style": {"full_width": True}},
    )

    # Saving as HTML File
    profile.to_file(
        output_file="output/{}.html".format(filename[:-4])
    )  # pop .csv from string

    # As a string
    json_data = profile.to_json()

    # As a file
    profile.to_file(
        output_file="output/{}.json".format(filename[:-4])
    )  # pop .csv from string

    print('SUCCESS! Pandas profile report created for file: {}'.format(filename))


def main():
    for file in FILES:
        generate_pandas_profile(file)


if __name__ == "__main__":
    main()
