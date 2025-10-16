# Part 2: Setting up Local Redis and Basic Stream Operations

## Installing Redis Locally

If Redis is not installed, you can install it using Homebrew on macOS:

```bash
brew install redis
```

Start Redis server:

```bash
redis-server
```

In a separate terminal, test the connection:

```bash
redis-cli ping
```

You should see `PONG` as response.

## Connecting with Python

We'll use the `redis-py` library. Install it if not already:

```bash
pip install redis
```

## Advanced Stream Operations

- Consumer Groups: Allow multiple consumers to read from the same stream
- Pending messages: Track messages that have been delivered but not acknowledged
- Trimming streams: Remove old entries to save memory