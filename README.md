# Data-Engineering-Project
Automated Data Pipeline – SQL Server to CSV, Parquet, Avro

Author: Md Shahzeb Safeel

Location: Kolkata, West Bengal

Domain: Data Engineering & Pipeline Automation

# Project Objective
This project implements a modular data pipeline that extracts relational data from SQL Server and exports it into multiple formats. It supports both time-based and event-based triggers to automate data flow for reporting, warehousing, and real-time processing.

Pipeline Stages:-
1. Data Extraction
        Connects to SQL Server (sales_db) using SQLAlchemy and PyODBC to fetch tabular data.

2. Data Export
        Converts and exports the data into:

        CSV: For broad compatibility

        Parquet: For efficient storage and analytics

        Avro: For compact, schema-evolution-ready serialization

3. Automation Triggers
          Event-based: Uses a monitored input/ folder. On file arrival, export_data.py is executed automatically.

          Schedule-based: Uses Windows Task Scheduler to run the pipeline at defined intervals.

4. Data Replication
          Full copy: Duplicates all tables from sales_db to sales_db_copy

          Selective copy: Transfers specific tables and columns for compliance or data minimization


Key Technologies
Python (Pandas, PyArrow, FastAvro, Watchdog)

SQL Server (via PyODBC & SQLAlchemy)

Windows Task Scheduler

Testing

Manual Run:
python export_data.py

Event Trigger:
Drop any .csv file in input/ to trigger export

Scheduled Trigger:
Set schedule_task.bat in Task Scheduler

Database Copy:

Full: python copy_full_db.py

Selective: python copy_selected_tables.py
