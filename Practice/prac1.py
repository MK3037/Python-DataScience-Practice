# loading csv into sql cause we cant filter in csv. and if use pandas to filter such huge data then it will take a day
import os
import pandas as pd
from sqlalchemy import create_engine
os.chdir('C:\\Users\\purve\\OneDrive\\Desktop\\project')

# 1. Setup database connection
db_user = 'root'
db_password = 'mihir'
db_host = 'localhost'
db_port = '3306'
db_name = 'project1'

connection_string = f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
engine = create_engine(connection_string)

# 2. Map file names to target SQL table names
datasets = {
    'customer': 'customers',
    'product': 'products',
    'transactions': 'transactions',
    'click_stream': 'click_stream',
}

chunk_size = 100_000

# 3. Loop through each file with robust parsing configurations
for file_name, table_name in datasets.items():
  file_path = f'{file_name}.csv'
  print(f'\nStarting import for: {file_name} -> table: {table_name}')

  first_chunk = True

  try:
    # Read and push in chunks
    for chunk in pd.read_csv(
        file_path,
        chunksize=chunk_size,
        low_memory=False,
        on_bad_lines='skip',  # Skips malformed rows instead of crashing
        encoding='utf-8',  # Standard encoding
    ):

      mode = 'replace' if first_chunk else 'append'
      chunk.to_sql(
          table_name,
          con=engine,
          if_exists=mode,
          index=False,
          chunksize=10_000,
      )

      first_chunk = False
      print(f'Processed and loaded chunk for {table_name}...')

  except Exception as e:
    print(f'Error processing {file_name}: {e}')

print('\nBatch import process finished!')