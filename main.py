from vanna.openai import OpenAI_Chat
from vanna.chromadb import ChromaDB_VectorStore

import os

import pandas as pd
import sqlite3
# Get the API key from environment variables
api_key = os.getenv("OPEN_API_KEY")
openai_api = api_key
class MyVanna(ChromaDB_VectorStore, OpenAI_Chat):
    def __init__(self, config=None):
        ChromaDB_VectorStore.__init__(self, config=config)
        OpenAI_Chat.__init__(self, config=config)

vn = MyVanna(config={'api_key': openai_api, 'model': 'gpt-4o'})

vn.connect_to_sqlite('retail_sales.db')

from vanna.flask import VannaFlaskApp
app = VannaFlaskApp(vn, allow_llm_to_see_data = True)
app.run()
