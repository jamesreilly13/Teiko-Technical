# James Reilly
# Teiko Technical - Part 1 Data Management
# A file to initialize and copy (from the .csv) our SQLite database.

import sqlite3
import pandas as pd
from pathlib import Path

DB_path = "db/cell_counts.db"
CSV_path = "cell-count.csv"

# A function that initializes our database based on the .csv schema.
def initialize_database():
    Path("db").mkdir(exist_ok=True)
    conn = sqlite3.connect(DB_path)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cell_counts (
        sample TEXT PRIMARY KEY,
        project TEXT,
        subject TEXT,
        condition TEXT,
        age INTEGER,
        sex TEXT,
        treatment TEXT,
        response TEXT,
        sample_type TEXT,
        time_from_treatment_start INTEGER,
        b_cell INTEGER,
        cd8_t_cell INTEGER,
        cd4_t_cell INTEGER,
        nk_cell INTEGER,
        monocyte INTEGER
    );
    """)

    conn.commit()
    conn.close()

# A function that utilizes SQLite to load our .csv information to our .db.
def load_csv_to_db():
    conn = sqlite3.connect(DB_path)
    df = pd.read_csv(CSV_path)

    df.to_sql(
        "cell_counts",
        conn,
        if_exists = "replace",
        index = False
    )

    conn.close()

if __name__ == "__main__":
    # function calling
    initialize_database()
    load_csv_to_db()
