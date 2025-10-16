import redis
import json
import time

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def process_task(task):
    task_id = task['id']
    stream_name = f'task_logs:{task_id}'

    # Log start
    r.xadd(stream_name, {'event': 'started', 'timestamp': str(time.time())})

    # Simulate processing
    time.sleep(1)
    r.xadd(stream_name, {'event': 'processing', 'step': 'step1'})

    time.sleep(1)
    r.xadd(stream_name, {'event': 'processing', 'step': 'step2'})

    # Log completion
    r.xadd(stream_name, {'event': 'completed', 'timestamp': str(time.time())})

    print(f"Processed task {task_id}")

while True:
    _, task_json = r.brpop('task_queue')
    task = json.loads(task_json)
    process_task(task)