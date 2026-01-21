# Teiko-Technical
A repository containing James Reilly's submission for the Teiko Technical.

# Loblaw Bio – Immune Cell Analysis Pipeline

This project implements a complete data analysis pipeline and interactive dashboard for immune cell profiling in a melanoma clinical trial evaluating the drug candidate miraclib. The goal is to enable analysis of immune cell populations, comparison of responders vs non-responders, and exploration of baseline cohort characteristics.

## Project Structure
├── data_management.py # Part 1: Database schema and CSV loading

├── analysis.py # Part 2: Compute relative frequencies of cell populations

├── stats_analysis.py # Part 3: Statistical comparison and visualization

├── queries.py # Part 4: Cohort queries and summaries

├── dashboard.py # Streamlit dashboard integrating all analyses

├── data/
│ └── cell-count.csv # Input CSV file

├── requirements.txt # Python dependencies

├── README.md

└── .gitignore

---
## How to Run the Project

This project is designed to be run locally or in GitHub Codespaces.

### 1. Install Dependencies

Make sure you have Python 3.11+ installed. Then:

```
pip install -r requirements.txt
```

```requirements.txt``` contains:

```
nginx
Copy code
pandas
numpy
scipy
matplotlib
seaborn
streamlit
```

## 2. Initialize the Database
```
python data_management.py
```
This creates the SQLite database (cell_counts.db) in the db/ folder.
Loads all data from cell-count.csv into the database.

## 3. Run Analyses
Optional, for inspection:
```
python analysis.py        # Part 2: Relative frequencies
python stats_analysis.py  # Part 3: Responder vs non-responder stats
python queries.py         # Part 4: Baseline cohort summaries
```

## 4. Launch the Dashboard
```
streamlit run dashboard.py
```
Opens an interactive web dashboard

Allows exploration of:
- Immune cell population frequencies
- Responder vs non-responder distributions
- Statistical significance (p-values)
- Baseline cohort summary
- Database Schema
  
The project uses a single table cell_counts in SQLite. Each row corresponds to a single biological sample.

# Design Rationale
1. Denormalized table simplifies analytics queries
2. Efficient for filtering by disease, sample type, treatment, or timepoint
3. Scales to hundreds of projects and thousands of samples
4. New cell types or metadata can be added as columns without changing the schema
5. Indexes can be added on key columns (condition, treatment, time_from_treatment_start) for performance

# Code Architecture

data_management.py – handles database creation and CSV ingestion
analysis.py – computes relative frequencies of cell populations
stats_analysis.py – performs statistical comparisons and creates boxplots
queries.py – retrieves baseline cohort data and generates descriptive statistics
dashboard.py – interactive Streamlit dashboard integrating all analyses

## Separation of concerns:

Data storage (SQLite) → isolated
Analysis & statistics → modular scripts
Visualization → dashboard only
This structure ensures reproducibility, maintainability, and scalability.

# Dashboard Overview
The dashboard allows users to:
- Inspect relative frequencies of all immune cell populations per sample
- Compare responders vs non-responders for melanoma PBMC samples
- View statistical significance for each immune population
- Explore baseline cohort characteristics (samples per project, sex, response)

To launch locally:
```
streamlit run dashboard.py
```

## Reproducibility Notes
All analyses are driven from the database (cell_counts.db), which can be regenerated from cell-count.csv. No results are hard-coded. Works in GitHub Codespaces or any local Python environment

## Optional Enhancements for Large-Scale Data
Migrate database from SQLite → PostgreSQL for multi-user access, normalize subject- and project-level metadata, add indexes and materialized views for faster queries, extend dashboard with filters for timepoints, populations, or treatment types.











