import pyodbc

source_conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost\\SQLEXPRESS;DATABASE=sales_db;Trusted_Connection=yes")

target_conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost\\SQLEXPRESS;DATABASE=sales_db_copy;Trusted_Connection=yes")


src_cursor = source_conn.cursor()
tgt_cursor = target_conn.cursor()


src_cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE'")
tables = src_cursor.fetchall()

for (table_name,) in tables:
    print(f"📋 Copying table: {table_name}")
    try:
        
        tgt_cursor.execute(f"IF OBJECT_ID('{table_name}', 'U') IS NOT NULL DROP TABLE {table_name}")
        tgt_cursor.execute(f"SELECT * INTO {table_name} FROM sales_db.dbo.{table_name}")
        target_conn.commit()
    except Exception as e:
        print(f"❌ Failed to copy {table_name}: {e}")

src_cursor.close()
tgt_cursor.close()
source_conn.close()
target_conn.close()
