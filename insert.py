import common
import psycopg2
from psycopg2 import sql
from openai import OpenAI

# Setup OpenAI client
client = OpenAI()

# List of texts to insert
texts_to_insert = [
    "The quick brown fox jumps over the lazy dog.",
    "Exploring the depths of the Mariana Trench reveals surprising biological diversity.",
    "Advances in artificial intelligence are transforming the tech landscape.",
    "Cooking at home can be both fun and challenging, especially when trying new recipes.",
    "The economic impact of global pandemics has reshaped international trade policies.",
    "Understanding quantum mechanics opens new frontiers in computing and cryptography.",
    "Sustainable agriculture practices contribute to a healthier environment.",
    "The history of classical music is rich with diverse composers and evolving styles.",
    "Innovations in renewable energy are crucial for addressing climate change.",
    "Physical exercise and mental well-being are closely interconnected."
]


def insert_texts(texts, connection_parameters):
    # Connect to your PostgreSQL database
    conn = psycopg2.connect(**connection_parameters)
    cur = conn.cursor()

    # SQL query to insert data
    insert_query = sql.SQL("INSERT INTO text_embeddings (embedding_text, embedding_vector) VALUES (%s, %s)")

    for text in texts:
        # Generate embedding for the text
        embedding = common.generate_embedding(text)

        # Execute the query for each text
        cur.execute(insert_query, (text,embedding))

    # Commit the transaction
    conn.commit()

    # Close the cursor and connection
    cur.close()
    conn.close()


# Insert the texts into the table
insert_texts(texts_to_insert, common.connection_parameters)
