from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data

default_args = {
    'owner': 'tris',
    'start_date': datetime(2025, 1, 1),
    'retries': 1
}

with DAG(
    dag_id='accidents_etl_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
) as dag:

    task_extract = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data
    )

    task_transform = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data
    )

    task_load = PythonOperator(
        task_id='load_data',
        python_callable=load_data
    )

    task_extract >> task_transform >> task_load