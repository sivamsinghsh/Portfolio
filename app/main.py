"""Starter application for 72ITDS30103 Software Development Platforms.

A deliberately small web API. You will containerise it in Lab 2,
connect it to PostgreSQL in Week 4, deploy it in Lab 3 and test it
in a pipeline from Week 6.
"""

import os
MISSING = os.environ["DEFINITELY_NOT_SET"]

from fastapi import FastAPI, HTTPException

APP_NAME = os.getenv("APP_NAME", "sdp-starter")
APP_VERSION = "0.3.0"

app = FastAPI(title=APP_NAME, version=APP_VERSION)

# In-memory data. Week 4 replaces this with a PostgreSQL table.
ITEMS = [
    {"id": 1, "name": "Write a Dockerfile", "done": False},
    {"id": 2, "name": "Run it with Compose", "done": False},
    {"id": 3, "name": "Deploy it to Render", "done": False},
]


@app.get("/")
def root():
    """Proves the app is reachable. Open /docs for the interactive API page."""
    return {"app": APP_NAME, "version": APP_VERSION, "message": "Hello from the starter app"}


@app.get("/health")
def health():
    """Used by Render (Lab 3) and the pipeline (Week 6) to check the app is alive."""
    return {"status": "ok"}


@app.get("/items")
def list_items():
    return ITEMS


@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in ITEMS:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")
