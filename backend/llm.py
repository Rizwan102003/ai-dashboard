import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

schema = """
Table: sales
Columns:
date
region
product
revenue
"""

def generate_sql(prompt):

    system_prompt = f"""
You are a SQL generator.

Database schema:
{schema}

Return ONLY SQL query.
"""

    response = model.generate_content(system_prompt + prompt)

    return response.text