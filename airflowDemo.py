from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator


def say_hi(who):
    return f"Hi {who}"


print(say_hi("XX"))


with DAG("my-dag", start_date=datetime(2024, 2, 19)) as dag:
    task1 = PythonOperator(
        task_id="first_task", python_callable=say_hi, op_kwargs={"who": "A"}
    )

    task2 = PythonOperator(
        task_id="second_task", python_callable=say_hi, op_kwargs={"who": "B"}
    )


task1 >> task2
