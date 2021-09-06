import logging

from celery import Celery
import datetime
from time import sleep
import requests

app = Celery('tasks', backend='redis://localhost', broker='redis://0.0.0.0:6379')


@app.task
def call_url(task_id):
    start_time = datetime.datetime.now()

    url = "https://hookb.in/mZpzNPM6eBhlzXNNzbOq"

    payload = {"task_id": task_id}
    try:
        response = requests.request("POST", url, data=payload)
        print(response.text)
    except Exception as e:
        print(e)

    time_taken = (datetime.datetime.now() - start_time).seconds
    print(f"Time taken: {time_taken} seconds")
    return True
