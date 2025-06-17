# Chinook Music Store SQL Project

This project explores customer music genre preferences using the Chinook database, a fictional dataset of digital music sales. The goal is to demonstrate intermediate SQL skills, exploratory analysis, and communication of data insights.

## Project Structure

- `ChinookSQLProject.ipynb` - the Jupyter notebook containing the SQL analysis and visualizations
- `ChinookSQLProject.html` - an HTML version of the Jupyter notebook that shows the content without needing to implement the code
- `input/` - contain a `.png` image used in the notebook
- `README.md` - this file

## Summary of Analysis

- Rock is the most popular genre globally, suggesting strong universal appeal.
- Country-specific preferences** were also found, suggesting the potential for localized marketing strategies.

*Note: This is a technical exercise using a small, fictional dataset and is not intended to reflect real-world music trends.*

## Getting Started

To run this notebook:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/chinook-sql-project.git
   cd chinook-sql-project
2. Set up a local MySQL server and import the Chinook database (available [here](https://github.com/lerocha/chinook-database))

3. Update the database connection string directly in the notebook
    ```python
    user = "your_username"
    password = "your_password"
    host = "localhost"
    port = 3306
    database = "chinook"

    # Create the SQLAlchemy engine
    engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")
4. Install dependencies:
    ```bash
    pip install -r requirements.txt
5. Launch Jupyter Lab or Notebook and open ChinookSQLProject.ipynb.ipynb.

## View the Notebook

- [Rendered view via nbviewer](https://nbviewer.org/) *(link to your notebook once uploaded)*

---

## Tools Used

- SQL (MySQL)
- Python:
  - Pandas
  - Numpy
  - SQLAlchemy
  - Matplotlib / Seaborn
- Jupyter Notebook

---

## Purpose

This project was completed as a portfolio piece to demonstrate:

- SQL proficiency with joins, grouping, and aggregation  
- Integration of SQL with Python  
- Data visualization and communication of business insights