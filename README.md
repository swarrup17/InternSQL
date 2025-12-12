# 🏏 Cricket Database Management System

A small workspace demonstrating SQLite database usage with `ipython-sql` in Jupyter Notebook, along with a Streamlit app for CRUD operations on cricket teams, players, matches, and statistics.

---

## 📂 Project Files

- `sqlpractice.ipynb` — Jupyter Notebook with table definitions, sample inserts, and SQL queries using `%sql` / `%%sql`.
- `.env`- required environment to hide confidential information 
- `requirements.txt` — Python dependencies for running both Jupyter and all  code

---

## ⚡ Quick Start
1. (Optional) Create and activate a virtual environment.
```bash
python -m venv .venv
```
2. Install dependencies:

```cmd
pip install -r requirements.txt
```

3. 📓 Running the Jupyter Notebook

Start Jupyter Lab or Notebook:
```
jupyter lab
# or
jupyter notebook
```
Open 
```
sqlpractice.ipynb
```

How query results are displayed
- ipython-sql renders query results automatically when you run `%sql` (single-line) or `%%sql` (cell) magic. However, the exact visual format depends on packages available in the kernel environment:
	- If `pandas` is available and ipython-sql can return a DataFrame, results may appear as HTML tables (rich display).
	- If `prettytable` is present (for example `prettytable==0.7.2`), ipython-sql will fall back to a plain-text pretty table rendering, which looks like an ASCII/terminal table inside the notebook output.

Examples (pure SQL):

```sql
%%sql
SELECT * FROM Players;
```

If you see a plain-text pretty table instead of an HTML DataFrame and you prefer HTML output, use one of these options described below.

Notes & troubleshooting
- Empty SELECT after INSERT: re-run create/insert cells or restart the kernel; ensure the same DB file is used by all cells.
- PermissionError removing DB file: close ipython-sql with `%sql -x` or restart the kernel before deleting the file.
- Mixing connection types: prefer a single approach (either SQLAlchemy `engine` or `sqlite3`) across your notebook to avoid confusion.

Why you're seeing plain-text pretty tables
- `ipython-sql` chooses a formatter based on what is available in the kernel environment. In this workspace the environment currently includes `prettytable`, so ipython-sql displays query results using a plain-text pretty table renderer. This is expected and not an error.

Options: keep prettytable or switch to HTML DataFrames

You can choose between keeping the current plain-text rendering or switching to HTML DataFrame output (recommended for notebooks):

- Keep `prettytable` (no change): run `%%sql SELECT ...` as you do now; results will appear as prettytable text blocks.

- Use pandas for guaranteed HTML tables (recommended): run SQL from a Python cell and let Jupyter render the DataFrame as HTML. Example:

```python
import sqlite3
import pandas as pd

conn = sqlite3.connect('Cricket.db')
df = pd.read_sql_query('SELECT * FROM Players;', conn)
df
conn.close()
```

- Remove `prettytable` so ipython-sql will prefer richer renderers: uninstall it from your environment or remove it from `requirements.txt` and reinstall packages. Example:

```powershell
pip uninstall prettytable
# or edit requirements.txt to remove the prettytable line, then
pip install -r requirements.txt
```

After changing installed packages, restart the kernel (Kernel → Restart) to apply the new renderer behavior.

Capturing `%sql` results into pandas

If you prefer to keep using `%sql` but want to render results as HTML, some ipython-sql versions let you convert the result to a DataFrame:

```python
res = %sql SELECT * FROM Players;
if hasattr(res, 'DataFrame'):
	df = res.DataFrame()
	df
else:
	# fallback: use pandas.read_sql_query
	import sqlite3, pandas as pd
	conn = sqlite3.connect('Cricket.db')
	df = pd.read_sql_query('SELECT * FROM Players;', conn)
	df
	conn.close()
```

If you want, I can update `requirements.txt` to remove `prettytable` and ensure `pandas` is listed, and/or add example cells to `sqlpractice.ipynb` that always show HTML DataFrame output.

Common commands
- Load the SQL extension:

```sql
%load_ext sql
```

- Connect to the local SQLite file used in this notebook:

```sql
%sql sqlite:///Cricket.db
```

- Close ipython-sql connections (safe before deleting DB file):

```sql
%sql -x
```

### 🛠 Recommended Environment Setup
- Python 3.10+
- Packages in `requirements.txt:`

`
pandas
`
`
ipython-sql
`
`
sqlalchemy
`
`
sqlite3
`
`
hashlib 
`
`
python-dotenv
`
# Migrated From sqlite to PostegreSql and Validation using checksum
# Load .env
`
load_dotenv("C:/Users/Swarup Dahal/Desktop/InternSQL/.env")
`

- Loads envirnment for database connection from .env file

`
MYSQL_CONN_STR = os.getenv("MYSQL_CONN_STR")
`

`
PG_CONN_STR = os.getenv("PG_CONN_STR")
`

- Connects to MySQL and PostgreSQL databases.

`
if not MYSQL_CONN_STR or not PG_CONN_STR: 
   raise ValueError("Connection strings not loaded from .env.")
`
- checks for if connection between mysql and postgresql is created or not
- if connection is not created then raise value erroe as connection  is not loaded dron .env 

# Create engines
```
mysql_engine = create_engine(MYSQL_CONN_STR)
pg_engine = create_engine(PG_CONN_STR)
```
# Migration Function

```
def migrate():
   df = pd.read_sql(f"SELECT * FROM {table_name}", mysql_engine)
   df.to_sql(table_name, pg_engine, if_exists="replace",   index=False)
```


Reads table from MySQL and writes it to PostgreSQL.

`def validate(table_name: str) -> bool:
`
This functions validates the if the data of mysql and postgresql matches or not.


```
checksum_mysql = hashlib.sha256()

    for row in df_mysql.itertuples(index=False):
        checksum_mysql.update(''.join(str(v) for v in row).encode())

checksum_pg = hashlib.sha256()
    for row in df_pg.itertuples(index=False):
        checksum_pg.update(''.join(str(v) for v in row).encode())
```
- Computes checksums row-by-row for both databases.
- Ensures even a single value mismatch is detected.

# Display checksum values
    mysql_checksum_value = checksum_mysql.hexdigest()
    pg_checksum_value = checksum_pg.hexdigest()

    print(f"MySQL checksum for {table_name}:{mysql_checksum_value}")
    print(f"PostgreSQL checksum for {table_name}:{pg_checksum_value}")
# Validates Using Checksum
    if mysql_checksum_value == pg_checksum_value:
        print(f"Validation PASSED for {table_name}: checksums match ")
        return True
    else:
        print(f"Validation FAILED for {table_name}: checksums do not match ")
        return False
- Checks the checksum value for both mysql and postgre sql
- Returns Validation Pass if Checksum Matches
- Returns Validation Fail if Checksum does not matches
# Main Function to read,migrate and validate tables
```
def main():
    tables = ["Teams", "Players", "Matches","BattingStats","BowlingStats"]  # add more tables as needed
    start_total = time.time()

    for table in tables:
        t_migrate = time.time()
        migrate_table(table)
        print(f"Time taken to migrate {table}: {time.time() - t_migrate:.4f} sec")

        t_validate = time.time()
        validate(table)
        print(f"Time taken to validate {table}: {time.time() - t_validate:.4f} sec")

    print(f"\nTotal time for all tables: {time.time() - start_total:.4f} sec")

if __name__ == "__main__":
    main()
```
# Example of migration and validation output
```
Starting migration for table: Teams
Finished migrating table: Teams (13 rows)
Time taken to migrate Teams: 0.1030 sec

Validating table: Teams
MySQL checksum for Teams:       dbed528c738e0f3880b08cb51fdd3112245bac776fbbb5207afe18336acb1a2a
PostgreSQL checksum for Teams:  dbed528c738e0f3880b08cb51fdd3112245bac776fbbb5207afe18336acb1a2a
Validation PASSED for Teams: checksums match 
Time taken to validate Teams: 0.0092 sec
```

# Optional: remove prettytable if you want HTML DataFrames

If you want me to add examples showing how to list all tables with a single SQL query or to insert these instructions into the top of `sqlpractice.ipynb`, tell me and I will make the change.
