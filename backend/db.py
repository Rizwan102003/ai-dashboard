import pandas as pd
import sqlite3

conn = sqlite3.connect("data.db", check_same_thread=False)

def load_data():
    df = pd.read_csv("../data/sales.csv", encoding="cp1252")
    df.to_sql("sales", conn, if_exists="replace", index=False)

def run_query(query):
    result = pd.read_sql_query(query, conn)
    return result.to_dict(orient="records")