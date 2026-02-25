# hello_world.py
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG("version_test", start_date=datetime(2024, 1, 1), schedule=None) as dag:
    BashOperator(task_id="print_ver", bash_command="echo 'I am Version 1'")
