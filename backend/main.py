from fastapi import FastAPI
from db import load_data, run_query
from llm import generate_sql

app = FastAPI()

load_data()

@app.post("/query")
def query_data(prompt: str):

    sql = generate_sql(prompt)

    try:
        data = run_query(sql)

        return {
            "sql": sql,
            "data": data
        }

    except Exception as e:

        return {
            "error": str(e)
        }