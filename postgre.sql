-- Open the PostgreSQL CLI
docker exec -it afc59be2ab2f psql -U postgres

-- Create the database
CREATE DATABASE vector_test;

-- Switch to the vector_test database
\c vector_test

-- Add the pg_vector extension
CREATE EXTENSION vector;

-- Create the table
CREATE TABLE text_embeddings (
    id SERIAL PRIMARY KEY,
    embedding_text TEXT,
    embedding_vector vector(1536)  -- OpenAI dimensions
);