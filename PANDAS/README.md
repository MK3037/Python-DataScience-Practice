# Pandas Practice — Organized

Your original 8 notebooks were full of duplicate "people" examples and mixed-up
topics. They've been reorganized into **7 topic-based notebooks**, in the order
you'd actually learn them, each with a `# SQL:` comment next to every pandas
line showing its closest **MySQL** equivalent.

## Notebook order

| # | File | Topic | Came from |
|---|------|-------|-----------|
| 1 | `01_series_and_dataframe_basics.ipynb` | Series vs DataFrame, building a DataFrame from a dict / list / NumPy array | panda0 |
| 2 | `02_reading_and_exploring_data.ipynb` | `read_csv`, `info`, `head`, `tail`, `shape`, `columns` | panda1 |
| 3 | `03_selecting_data_loc_iloc.ipynb` | `iloc` vs `loc`, `set_index`, `reset_index` | panda1, panda2 |
| 4 | `04_filtering_data.ipynb` | Boolean masks, `&` `|` `~`, `.isin()`, `.str.contains()` | pandas3, pandas4 |
| 5 | `05_sorting_data.ipynb` | `sort_values`, `sort_index` | pandas7 |
| 6 | `06_updating_rows_and_columns.ipynb` | Renaming columns, editing values, `.apply()`, `.map()`, `.replace()` | pandas5 |
| 7 | `07_adding_removing_rows_and_columns.ipynb` | Adding/splitting columns, `pd.concat`, `.drop()` | pandas6 |

Duplicate copies of the same `people` DataFrame example (which appeared
almost identically in pandas3, pandas5, pandas6, and pandas7) were consolidated
so each notebook is self-contained without redundant repeats.

## Quick pandas ↔ SQL cheat sheet

| Pandas | SQL |
|---|---|
| `df.head(5)` | `SELECT * FROM t LIMIT 5;` |
| `df.shape` | `SELECT COUNT(*) FROM t;` (+ column count) |
| `df.columns` | `SELECT column_name FROM information_schema.columns WHERE table_name='t';` |
| `df[['a','b']]` | `SELECT a, b FROM t;` |
| `df.loc[filt]` / `df[filt]` | `SELECT * FROM t WHERE ...;` |
| `df.loc[filt, ['a']]` | `SELECT a FROM t WHERE ...;` |
| `df['a'].isin([...])` | `a IN (...)` |
| `df['a'].str.contains('x')` | `a LIKE '%x%'` |
| `df.sort_values(by='a')` | `ORDER BY a;` |
| `df.sort_values(by=['a','b'], ascending=[False,True])` | `ORDER BY a DESC, b ASC;` |
| `df.set_index('a')` | conceptually `ADD PRIMARY KEY (a)` |
| `df.rename(columns={...})` | `ALTER TABLE t RENAME COLUMN ...;` (MySQL 8.0.19+) |
| `df.loc[filt,'a'] = val` | `UPDATE t SET a = val WHERE ...;` |
| `df['a'] = df['a'].str.lower()` | `UPDATE t SET a = LOWER(a);` |
| `df['a'].str.split(' ')` | `SUBSTRING_INDEX(a, ' ', 1)` / `SUBSTRING_INDEX(a, ' ', -1)` |
| `df.drop(columns=['a'])` | `ALTER TABLE t DROP COLUMN a;` |
| `pd.concat([df, new_row])` | `INSERT INTO t VALUES (...);` |
| `df.drop(index=3)` | `DELETE FROM t WHERE id = 3;` |
| `df.info()` | `DESCRIBE t;` or `SHOW COLUMNS FROM t;` |
| `pd.read_csv('f.csv')` | `LOAD DATA INFILE 'f.csv' INTO TABLE t ...;` |

MySQL note: quote column names with spaces using backticks (`` `FIRST NAME` ``),
not double quotes like Postgres.

## A couple of things worth remembering (mixed up often)

- **`loc` vs `iloc`**: `loc` uses row/column **labels** and is inclusive on
  slices; `iloc` uses integer **positions**, like SQL's `LIMIT`/`OFFSET`.
- SQL tables are conceptually **unordered** — "row 3" only means something
  once you `ORDER BY` something, whereas a DataFrame always has a row order.
- `.apply()` / `.map()` (functions applied per column or per cell) don't have
  a clean SQL equivalent — SQL only has per-row expressions like `CASE`,
  built-in functions (`LOWER`, `UPPER`, `CONCAT`), and aggregate functions
  (`MIN`, `MAX`, `COUNT`).
