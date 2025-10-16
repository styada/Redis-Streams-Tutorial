import redis

# Connect to local Redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Add entries to a stream
stream_name = 'mystream'
r.xadd(stream_name, {'field1': 'value1', 'field2': 'value2'})
r.xadd(stream_name, {'field1': 'value3', 'field2': 'value4'})

# Read entries from the stream
entries = r.xrange(stream_name, '-', '+')
for entry_id, fields in entries:
    print(f"ID: {entry_id}, Fields: {fields}")

# Read from the stream starting from a specific ID
new_entries = r.xread({stream_name: '0-0'}, count=10)
for stream, messages in new_entries:
    for message_id, message_data in messages:
        print(f"Stream: {stream}, ID: {message_id}, Data: {message_data}")