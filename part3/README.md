# Part 3: Integrating Redis Streams with Task Queue

In this part, we'll create a simple task queue using Redis lists and integrate it with streams for logging.

## Task Queue Basics

- Use Redis lists as queues: `LPUSH` to add tasks, `BRPOP` to consume tasks
- Each task will have an associated stream for logging activities

## Architecture

1. Producer adds tasks to queue
2. Consumer picks up task, creates a stream for it
3. Logs activities to the stream
4. Consumer processes the task