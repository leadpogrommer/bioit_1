import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator
# from airflow.operators.

with DAG(
    dag_id="hello_world",
    start_date=datetime.datetime(2021, 1, 1),
    schedule=None,
    catchup=False
):
    BashOperator(
        task_id='hello_task',
        bash_command='echo "Hello Airflow (more like sh*tflow)"'
    )