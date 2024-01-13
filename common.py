import time
from openai import OpenAI

# Setup OpenAI client
client = OpenAI()

# Database connection parameters
connection_parameters = {
    "dbname": "vector_test",
    "user": "postgres",
    "password": "example",
    "host": "localhost",
    "port": 5432 
}

def generate_embedding(text):
    print(f"Getting embedding for \"{text}\"...")
    start_time = time.time()

    response = client.embeddings.create(
        input=text,
        model="text-embedding-ada-002"
    )

    execution_time = time.time() - start_time
    tokens = response.usage.total_tokens
    print(f"The operation took {execution_time} seconds to execute and used {tokens} tokens.")

    return response.data[0].embedding
