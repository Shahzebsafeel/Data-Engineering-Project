import pyodbc


source_conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost\\SQLEXPRESS;DATABASE=sales_db;Trusted_Connection=yes"
)
target_conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost\\SQLEXPRESS;DATABASE=sales_db_copy;Trusted_Connection=yes"
)

src_cursor = source_conn.cursor()
tgt_cursor = target_conn.cursor()


copy_plan = {
    "customers": ["customer_id", "name", "signup_date"]
}

for table, columns in copy_plan.items():
    cols = ", ".join(columns)
    try:
        print(f"📦 Copying selected columns from {table}")
        
        
        tgt_cursor.execute(f"IF OBJECT_ID('{table}', 'U') IS NOT NULL DROP TABLE {table}")
        target_conn.commit()

        tgt_cursor.execute(f"""
            SELECT {cols}
            INTO {table}
            FROM sales_db.dbo.{table};
        """)
        target_conn.commit()
    except Exception as e:
        print(f"❌ Error copying {table}: {e}")

src_cursor.close()
tgt_cursor.close()
source_conn.close()
target_conn.close()

print("✅ Selective data copy completed.")
