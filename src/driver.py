from tasks import call_url
from celery import group
import datetime
import sys


def main(args):
    num_queues = int(args[0]) if args else 1
    num_items = int(args[1]) if args else 1
    print(f"Total Queues: {num_queues}\nTasks per queue: {num_items}")

    start_time = datetime.datetime.now()
    job = group([call_url.s(f"task: {y}-{i}").set(queue=f"queue_{y}") for i in range(num_items) for y in range(num_queues)])
    res = job.apply_async()

    res.join()

    time_taken = (datetime.datetime.now() - start_time).seconds
    print(f"Time taken: {time_taken} seconds")


if __name__ == '__main__':
    args = sys.argv[1:]
    main(args)
