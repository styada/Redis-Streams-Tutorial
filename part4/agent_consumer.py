import redis
import json
import time
import random

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def mock_llm_response(prompt):
    # Mock LLM response
    responses = [
        "Based on the data, I recommend processing step A first.",
        "The analysis shows potential issues in section B.",
        "Chain of thought: First check prerequisites, then execute main logic."
    ]
    return random.choice(responses)

def log_to_stream(stream_name, event_type, data):
    r.xadd(stream_name, {
        'event': event_type,
        'timestamp': str(time.time()),
        'data': json.dumps(data)
    })

def process_agent_task(task):
    task_id = task['id']
    stream_name = f'agent_logs:{task_id}'

    log_to_stream(stream_name, 'task_started', {'task_id': task_id, 'type': task['data']['type']})

    # Simulate agent thinking
    prompt = f"Process task: {task['data']}"
    log_to_stream(stream_name, 'chain_of_thought', {'step': 'analyzing_task', 'prompt': prompt})

    llm_response = mock_llm_response(prompt)
    log_to_stream(stream_name, 'llm_response', {'response': llm_response})

    # Simulate tool usage
    log_to_stream(stream_name, 'tool_usage', {'tool': 'data_processor', 'action': 'load_file', 'file': task['data']['payload'].get('file', 'unknown')})

    time.sleep(0.5)
    log_to_stream(stream_name, 'tool_usage', {'tool': 'data_processor', 'action': 'process_data', 'status': 'success'})

    # Simulate more thinking
    log_to_stream(stream_name, 'chain_of_thought', {'step': 'evaluating_results', 'thought': 'Results look good, proceeding to finalize'})

    log_to_stream(stream_name, 'task_completed', {'task_id': task_id, 'status': 'success'})

    print(f"Processed agent task {task_id}")

while True:
    _, task_json = r.brpop('task_queue')
    task = json.loads(task_json)
    process_agent_task(task)