#! /bin/bash

NUM_WORKERS=${1}
COUNTER=0

while [ ${COUNTER} -lt "${NUM_WORKERS}" ]; do
  echo "${COUNTER}"

  celery -A tasks worker --loglevel=INFO --pool=prefork --concurrency=8 -n worker_${COUNTER} --queues queue_${COUNTER} --detach

  let COUNTER=${COUNTER}+1
done
