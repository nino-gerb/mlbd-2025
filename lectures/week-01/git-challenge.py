#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

def person_a():
    """Reads the data in data/school_performance.csv
    and returns a dataframe with the first 5,000 rows.

    Returns:
    dataframe: containing first 5,000 rows of school_performace.csv
    """
    # Code goes over here.
    df = pd.read_csv(filepath_or_buffer="../../data/school_performance.csv")
    return df.head(5000)

def person_b(df):
    """Keeps only the data from the female students. 
    Where the column "gender" equals "female". P

    Parameters:
    df (dataframe): First 5,000 rows of school_performace.csv

    Returns:
    dataframe: Data from the female students
    """
    # Code goes over here.
    return df[df["gender"] == "female"]


def person_c(df):
    """Calculates the mean from the column "grade"

    Parameters:
    df (dataframe): Data from female students

    Returns:
    float: Mean grade
    """
    # Code goes over here.
    return np.mean(df["grade"])

def main():
    """ Main program """
    # Code goes over here.
    df = person_a()
    df = person_b(df)
    res = person_c(df)

    print(f"Mean grade of female students is {res}")

if __name__ == "__main__":
    main()
