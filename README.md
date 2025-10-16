# Redis Streams Tutorial

A 5-part tutorial for learning Redis Streams with a focus on agent task management and real-time logging.

## Tutorial Parts

1. [Introduction to Redis Streams](part1/) - Basic concepts and operations
2. [Setting up Local Redis](part2/) - Installation and advanced operations
3. [Task Queue Integration](part3/) - Basic producer-consumer with streams
4. [Agent Task Logging](part4/) - Detailed logging of agent activities
5. [Streaming Responses](part5/) - Real-time streaming to users

## Prerequisites

- Local Redis instance running
- Python 3.x with `redis` library (`pip install redis`)

## Running the Examples

Each part contains Python scripts. Run them in order:

```bash
cd part1
python basic_streams.py

cd ../part2
python consumer_groups.py

# And so on...
```

This tutorial demonstrates how to attach Redis Streams to background tasks for logging agent chain of thought, tool usage, and streaming responses back to users.
