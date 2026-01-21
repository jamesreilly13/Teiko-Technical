# James Reilly
# Teiko Technical - Part 3 Statistics
# This file provides the functionality needed to compare the differences in cell population relative 
# frequencies of melanoma patient responders versus non-responders. It also allows for boxplot visualization
# and reporting.

import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import mannwhitneyu

DB_PATH = "db/cell_counts.db"

POPULATIONS = [
    "b_cell",
    "cd4_t_cell",
    "cd8_t_cell",
    "nk_cell",
    "monocyte"
]

# function utilized to determine melanoma patient responders v. non-responders
def load_pbmc_summary(): 
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("""
        SELECT *
        FROM cell_counts
        WHERE condition = 'melanoma' 
        AND sample_type = 'PBMC'
        AND treatment = 'miraclib'
    """, conn)
    conn.close()

    df["total_count"] = df[POPULATIONS].sum(axis=1) # total immune cells per sample

    long_df = df.melt(
        id_vars=["sample", "response", "total_count"],
        value_vars=POPULATIONS,
        var_name="population",
        value_name="count"
    )

    long_df["percentage"] = ( # each row is one population in the sample (includes response to differentiate later)
        long_df["count"] / long_df["total_count"] * 100
    )

    return long_df

# Function to create boxplots for each immune population. Splits by response ("yes" or "no")
def responder_boxplot_figure(long_df):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(
        data=long_df,
        x="population",
        y="percentage",
        hue="response",
        ax=ax
    )
    ax.set_title("Immune Cell Relative Frequencies: Responders vs Non-Responders")
    ax.set_ylabel("Relative Frequency (%)")
    ax.set_xlabel("Cell Population")
    fig.tight_layout()
    return fig

def statistical_tests(long_df):
    results = [] # preparing p-value collection per population

    for pop in POPULATIONS:
        responders = long_df[ # responders split
            (long_df["population"] == pop) &
            (long_df["response"] == "yes")
        ]["percentage"]

        non_responders = long_df[ # non-responders split
            (long_df["population"] == pop) &
            (long_df["response"] == "no")
        ]["percentage"]

        # performs a Mann-Whittney U-Test
        # utilized to test if responder/non-responder distributions 
        # differ significantly.
        stat, p = mannwhitneyu(
            responders,
            non_responders,
            alternative="two-sided"
        )

        # save results of Mann-Whitney
        results.append({
            "population": pop,
            "p_value": p
        })

    return pd.DataFrame(results)

if __name__ == "__main__":
    # Execute script
    data = load_pbmc_summary()
    responder_boxplot_figure(data)
    stats = statistical_tests(data)
    print(stats)

