import common
import psycopg2
from psycopg2 import sql

def query_embedding_vector(target_embedding, connection_parameters, top_n=2):
    # Connect to your PostgreSQL database
    conn = psycopg2.connect(**connection_parameters)
    cur = conn.cursor()

    # SQL query to find the nearest neighbors by L2 distance
    # Test also with inner product (<#>) and cosine distance (<=>)
    query = sql.SQL("""
        SELECT id, embedding_text, embedding_vector <-> %s AS distance
        FROM text_embeddings
        ORDER BY distance
        LIMIT %s;
    """)

    # Format the embeddings to string
    formatted_target_embedding = '[' + ','.join(map(str, target_embedding)) + ']'

    # Execute the query with the target embedding and the number of results you want
    cur.execute(query, (formatted_target_embedding, top_n))

    # Fetch the results
    results = cur.fetchall()

    # Close the cursor and connection
    cur.close()
    conn.close()

    return results

# Ask for the query
user_input = input("What do you want to query? ")

# Your target embedding vector (query converted to vector)
target_embedding = common.generate_embedding(user_input)

# Query the embeddings
results = query_embedding_vector(target_embedding, common.connection_parameters)

# Print the results
print(f"\nResponse to the query \"{user_input}\":")
for result in results:
    print(f"\t{result[1]} (distance: {result[2]})")
