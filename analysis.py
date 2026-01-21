# James Reilly
# Teiko Technical - Part 2 Initial Analysis
# A file meant to answer the question -
# "What is the frequency of each cell type in each sample?"

import sqlite3
import pandas as pd

DB_path = "db/cell_counts.db" # our preexisting database (see part 1)

# cell types
POPULATIONS = {
    "b_cell",
    "cd4_t_cell",
    "cd8_t_cell",
    "nk_cell",
    "monocyte"
}

# A function that converts our table to long format and calculates cell type frequencies
def compute_relative_frequencies():
    conn = sqlite3.connect(DB_path)

    df = pd.read_sql("SELECT * FROM cell_counts", conn)
    conn.close()

    df["total_count"] = df[POPULATIONS].sum(axis=1)

    # converts DataFrame to long format (no longer one column per population)
    long_df = df.melt(
        id_vars=["sample", "total_count"],
        value_vars=POPULATIONS,
        var_name="population",
        value_name="count"
    )

    long_df["percentage"] = ( # add percentage column - calculates frequency
        long_df["count"] / long_df["total_count"] * 100
    )

    return long_df[ # return new dataframe with specified parameters from Part 2
        ["sample", "total_count", "population", "count", "percentage"]
    ]

if __name__ == "__main__":
    # run initial analysis
    summary = compute_relative_frequencies()
    print(summary.head())
