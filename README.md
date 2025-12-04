# Cricket Database SQL & Streamlit App

A small workspace demonstrating SQLite database usage with `ipython-sql` in Jupyter, along with a Streamlit app for CRUD operations on cricket teams, players, matches, and stats.

---

## Project Files

- `sqlpractice.ipynb` — Jupyter Notebook with table definitions, sample inserts, and queries using `%sql` / `%%sql`.
- `app.py` — Streamlit application for managing the cricket database.
- `requirements.txt` — Python dependencies for running both Jupyter and Streamlit.

---

## Quick Start

### 1. (Optional) Create and activate a virtual environment

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
2. Install dependencies
bash
Copy code
pip install -r requirements.txt
Running the Jupyter Notebook
Start Jupyter Lab or Notebook:

bash
Copy code
jupyter lab
# or
jupyter notebook
Open sqlpractice.ipynb.

How query results are displayed
%sql and %%sql magics automatically render query results.

Format depends on installed packages:

HTML DataFrame (recommended): requires pandas.

Plain-text table (prettytable): requires prettytable.

Example SQL query:
sql
Copy code
%%sql
SELECT * FROM Players;
Switching from prettytable to HTML tables
Capture %sql results into a DataFrame:

python
Copy code
res = %sql SELECT * FROM Players;
if hasattr(res, 'DataFrame'):
    df = res.DataFrame()
    df
Remove prettytable from your environment:

bash
Copy code
pip uninstall prettytable
Or query directly with Pandas:

python
Copy code
import sqlite3
import pandas as pd

conn = sqlite3.connect('Cricket.db')
df = pd.read_sql_query('SELECT * FROM Players;', conn)
df
conn.close()
Common %sql commands
sql
Copy code
%load_ext sql
%sql sqlite:///Cricket.db
%sql -x  # close connection
Running the Streamlit App (app.py)
app.py provides a web interface to manage Teams, Players, Matches, Batting Stats, and Bowling Stats.

Start the Streamlit server:

bash
Copy code
streamlit run app.py
A browser tab will open automatically.

Use the sidebar menu to:

Select a table (Teams, Players, Matches, Batting Stats, Bowling Stats)

Choose Dashboard to see a summary

Or perform CRUD operations on the selected table.

Notes
Initialize the database once using the app or Jupyter Notebook.

Restart the kernel if database changes are not reflected.

Always use the same SQLite file (Cricket.db) across Notebook and app.

For best experience in Jupyter, use HTML tables by having pandas installed and prettytable removed.

Recommended Environment Setup
Python 3.10+

Packages in requirements.txt:

txt
Copy code
streamlit
pandas
ipython-sql
sqlalchemy
sqlite3
# Optional: remove prettytable if you want HTML DataFrames