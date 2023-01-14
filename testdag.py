from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

def testmydag():
    return 'Testing DAG'

dag = DAG('dag_testing', description='Hello World DAG',
          schedule_interval='0 * * * *',
          start_date=datetime(2023, 1, 11), catchup=False)

test_operator = PythonOperator(task_id='dag_test_task', python_callable=testmydag, dag=dag)

test_operator