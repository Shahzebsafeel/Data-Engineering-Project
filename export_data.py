from sqlalchemy import create_engine
import pandas as pd
from fastavro import writer
import pyarrow.parquet as pq
import pyarrow as pa
import os
import datetime


engine = create_engine(
    r"mssql+pyodbc://localhost\SQLEXPRESS/sales_db?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
)


df = pd.read_sql("SELECT * FROM customers", engine)


for col in df.columns:
    if df[col].dtype == 'datetime64[ns]' or isinstance(df[col].dropna().iloc[0], (datetime.datetime, datetime.date)):
        df[col] = df[col].astype(str)


os.makedirs("output", exist_ok=True)


df.to_csv("output/customers.csv", index=False)


pq.write_table(pa.Table.from_pandas(df), "output/customers.parquet")


def infer_avro_schema(df):
    fields = []
    for col in df.columns:
        dtype = df[col].dtype
        if dtype == "int64":
            typ = "int"
        elif dtype == "float64":
            typ = "float"
        else:
            typ = "string"
        fields.append({"name": col, "type": [typ, "null"]})
    return {"name": "customers", "type": "record", "fields": fields}


records = df.to_dict(orient="records")
with open("output/customers.avro", "wb") as f:
    writer(f, infer_avro_schema(df), records)

print("✅ Data export completed: CSV, Parquet, and Avro files saved in './output'")
