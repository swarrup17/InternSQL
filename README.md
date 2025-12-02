# SQL Practice Notebook

A small workspace with a Jupyter notebook demonstrating using SQLite and `ipython-sql` magic inside Jupyter.

Files
- `sqlpractice.ipynb` — Jupyter Notebook with table definitions, sample inserts and queries using only `%sql` / `%%sql` and a few helper Python cells.
- `requirements.txt` — Recommended Python packages for running the notebook (Jupyter, `ipython-sql`, plotting libraries, etc.).

Quick start
1. (Optional) Create and activate a virtual environment.
2. Install dependencies:

```cmd
pip install -r requirements.txt
```

3. Start Jupyter Lab or Notebook and open `sqlpractice.ipynb`:

```powershell
jupyter lab
# or
jupyter notebook
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
- `ipython-sql` chooses a formatter based on the environment. If `prettytable` is installed and used, results are rendered in that format. That is normal and not an error.

Ways to get HTML DataFrame output (recommended)

1) Preferred — use `pandas.read_sql()` in a Python cell (no prettytable, guaranteed HTML rendering):

```python
import sqlite3
import pandas as pd

conn = sqlite3.connect('Cricket.db')
df = pd.read_sql_query('SELECT * FROM Players;', conn)
df  # Jupyter will render this as an HTML table
conn.close()
```

2) Capture ipython-sql result and convert to pandas if supported:

```python
res = %sql SELECT * FROM Players;
# many ipython-sql versions expose a DataFrame conversion
if hasattr(res, 'DataFrame'):
	df = res.DataFrame()
	df
else:
	print('Conversion to DataFrame not available; use pandas.read_sql_query instead.')
```

3) Remove or avoid installing `prettytable` in the kernel environment so ipython-sql will prefer richer renderers. To remove it from your dependencies, edit `requirements.txt` and remove the `prettytable` entry, then reinstall dependencies in your environment.

4) Restart the kernel after changing installed packages so the new rendering behavior takes effect.

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

If you want me to add examples showing how to list all tables with a single SQL query or to insert these instructions into the top of `sqlpractice.ipynb`, tell me and I will make the change.
