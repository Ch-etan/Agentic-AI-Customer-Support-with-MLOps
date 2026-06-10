memory_store = []

def add_to_memory(query, response):
    memory_store.append({"query": query, "response": response})

def get_memory():
    return memory_store[-3:]  # last 3 conversations