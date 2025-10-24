# Chinook Music Store SQL Project

This project explores customer music genre preferences using the Chinook database, a fictional dataset of digital music sales. The goal is to demonstrate SQL skills, exploratory analysis, and communication of data insights.

## Project Structure

- `notebooks/ChinookSQLProject.ipynb` - the Jupyter notebook containing the SQL analysis and visualizations
- `docs/ChinookSQLProject.html` - an HTML version of the Jupyter notebook that shows the content without needing to implement the code
- `input/` - contains a `.png` image used in the notebook
- `README.md` - this file

## Summary of Analysis

- Rock appears as the most popular genre in the sample data, suggesting broad appeal.
- Country-specific preferences were also found, suggesting the potential for localized marketing strategies.

*Note: This is a technical exercise using a small, fictional dataset and is not intended to reflect real-world music trends.*

## Getting Started

To run this notebook:

1. Clone the repository:
   ```bash
   git clone https://github.com/bpgodsil/chinook-sql-project.git
   cd chinook-sql-project
   ```

2. Ensure the Chinook SQLite database is available
   The notebook expects a file named Chinook_Sqlite.sqlite in the data/ directory.
   You can download it from the [Chinook Database repository](https://github.com/lerocha/chinook-database)

3. Verify the database connection
   The notebook assumes it is run from within the notebooks/ folder so that relative paths resolve correctly.
    ```python
    from pathlib import Path
    from sqlalchemy import create_engine

    repo_root = Path().resolve().parent
    DB_PATH = repo_root / "data" / "Chinook_Sqlite.sqlite"

    engine = create_engine(f"sqlite:///{DB_PATH}")
   ```

4. Install dependencies:
    ```bash
    pip install -r requirements.txt
   ```

5. Launch Jupyter Lab or Notebook and open ChinookSQLProject.ipynb
   ```bash
   jupyter lab
   ```

## View the Notebook

- [Rendered view via nbviewer](https://nbviewer.org/github/bpgodsil/sql-chinook-project/blob/main/notebooks/ChinookSQLProject.ipynb) 

---

## Tools Used

- SQL (SQLite)
- Python:
  - Pandas
  - Numpy
  - SQLAlchemy
  - Matplotlib / Seaborn
- Jupyter Notebook

---

## Purpose

This project was completed as a portfolio piece to demonstrate:

- SQL proficiency with joins, grouping, aggregation, and CTEs  
- Integration of SQL with Python  
- Data visualization and communication of business insights