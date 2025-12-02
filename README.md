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

If you want me to add examples showing how to list all tables with a single SQL query or to insert these instructions into the top of `sqlpractice.ipynb`, tell me and I will make the change.

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

If you want me to add examples showing how to list all tables with a single SQL query or to insert these instructions into the top of `sqlpractice.ipynb`, tell me and I will make the change.

