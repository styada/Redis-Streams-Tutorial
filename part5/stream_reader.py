import redis
import json
import time

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def stream_task_logs(task_id):
    stream_name = f'agent_logs:{task_id}'
    last_id = '0'

    print(f"Streaming logs for task {task_id}:")

    while True:
        entries = r.xread({stream_name: last_id}, block=1000)
        if entries:
            for stream, messages in entries:
                for msg_id, msg_data in messages:
                    event = json.loads(msg_data['data'])
                    print(f"[{msg_data['timestamp']}] {msg_data['event']}: {event}")
                    last_id = msg_id

                    # Check if task is completed
                    if msg_data['event'] == 'task_completed':
                        print("Task completed. Stopping stream.")
                        return
        else:
            time.sleep(0.1)

# Example usage - in real app, this would be triggered when user requests to watch a task
if __name__ == "__main__":
    task_id = input("Enter task ID to stream: ")
    stream_task_logs(task_id)