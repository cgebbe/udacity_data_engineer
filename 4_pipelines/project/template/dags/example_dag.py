# Simple DAG pipeline
import logging
import pendulum
from airflow.decorators import dag, task

@dag(start_date=pendulum.now(), schedule_interval="@daily")
def flow_dag():

    @task
    def hello():
        logging.info("Hello World!")

    hello()

# NOTE: calling DAG and assigning to value somehow required?!
dag=flow_dag()