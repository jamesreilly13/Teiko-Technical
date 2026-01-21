# James Reilly
# Teiko Technical - Part 4 Queries
# A file meant to query the database to answer Part 4's questions.

import sqlite3
import pandas as pd

DB_PATH = "db/cell_counts.db"

# Function to establish baseline cohort
def baseline_melanoma_pbmc():
    conn = sqlite3.connect(DB_PATH)

    # identifiers of cohort (condition, sample_type, etc.)
    df = pd.read_sql(""" 
        SELECT *
        FROM cell_counts
        WHERE condition = 'melanoma'
          AND sample_type = 'PBMC'
          AND treatment = 'miraclib'
          AND time_from_treatment_start = 0
    """, conn)

    conn.close()
    return df # return cohort

# Function to 
def summary_statistics(df):
    return {
        "samples_per_project": df["project"].value_counts(), # how many samples contributed per project 
        "subjects_response": df.groupby("response")["subject"].nunique(), # unique patients (responder vs. non-responder)
        "subjects_sex": df.groupby("sex")["subject"].nunique() # subjects by sex
    }

if __name__ == "__main__":
    baseline_df = baseline_melanoma_pbmc()
    summaries = summary_statistics(baseline_df)

    for name, result in summaries.items():
        print(f"\n{name.upper()}")
        print(result)
