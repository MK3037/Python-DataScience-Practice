import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///Foreign.db", echo=True)

df=pd.read_sql("select *from people", con=engine)
print(df)

new_data=pd.DataFrame({'name':['Dollar', 'Ruppe'], 'age':[1, 96]})
new_data.to_sql('people', con=engine, if_exists='append',index=False)