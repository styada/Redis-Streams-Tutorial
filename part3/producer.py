import redis
import json

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def add_task(task_data):
    task_id = r.incr('task_id_counter')
    task = {'id': task_id, 'data': task_data}
    r.lpush('task_queue', json.dumps(task))
    print(f"Added task {task_id}")

# Add some sample tasks
add_task({'type': 'process_data', 'payload': {'file': 'data.csv'}})
add_task({'type': 'send_email', 'payload': {'to': 'user@example.com'}})