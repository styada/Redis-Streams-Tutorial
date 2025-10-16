import redis
import time

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

stream_name = 'task_stream'
group_name = 'task_consumers'

# Create consumer group
try:
    r.xgroup_create(stream_name, group_name, id='0', mkstream=True)
except redis.ResponseError:
    pass  # Group already exists

# Add some tasks
for i in range(5):
    r.xadd(stream_name, {'task': f'task_{i}', 'data': f'data_{i}'})

# Consumer reading from group
consumer_name = 'consumer1'
messages = r.xreadgroup(group_name, consumer_name, {stream_name: '>'}, count=1)

for stream, msgs in messages:
    for msg_id, msg_data in msgs:
        print(f"Consumed: {msg_data}")
        # Acknowledge the message
        r.xack(stream_name, group_name, msg_id)

# Check pending messages
pending = r.xpending(stream_name, group_name)
print(f"Pending messages: {pending}")