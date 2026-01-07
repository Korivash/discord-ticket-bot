from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# Data Models (Pydantic)
class Server(BaseModel):
    server_id: str
    name: str
    configuration: dict

class Category(BaseModel):
    category_id: str
    server_id: str
    name: str
    description: str

class Ticket(BaseModel):
    ticket_id: str
    server_id: str
    title: str
    description: str
    user_id: str
    status: str
    priority: str

class KnowledgeBaseArticle(BaseModel):
    article_id: str
    server_id: str
    title: str
    content: str

# Placeholder data (replace with database integration)
servers = {}
categories = {}
tickets = {}
knowledge_base = {}

# API Endpoints
@app.get("/servers")
async def list_servers():
    return list(servers.values())

@app.get("/servers/{server_id}")
async def get_server(server_id: str):
    if server_id not in servers:
        raise HTTPException(status_code=404, detail="Server not found")
    return servers[server_id]

@app.post("/servers", response_model=Server)
async def create_server(server: Server):
    servers[server.server_id] = server
    return server

@app.get("/servers/{server_id}/categories")
async def list_categories(server_id: str):
    return [category for category in categories.values() if category.server_id == server_id]

@app.post("/servers/{server_id}/categories", response_model=Category)
async def create_category(server_id: str, category: Category):
    if category.server_id != server_id:
        raise HTTPException(status_code=400, detail="Server ID mismatch")
    categories[category.category_id] = category
    return category

@app.get("/servers/{server_id}/categories/{category_id}")
async def get_category(server_id: str, category_id: str):
    if category_id not in categories or categories[category_id].server_id != server_id:
        raise HTTPException(status_code=404, detail="Category not found")
    return categories[category_id]

@app.get("/servers/{server_id}/tickets")
async def list_tickets(server_id: str):
    return [ticket for ticket in tickets.values() if ticket.server_id == server_id]

@app.post("/servers/{server_id}/tickets", response_model=Ticket)
async def create_ticket(server_id: str, ticket: Ticket):
    if ticket.server_id != server_id:
        raise HTTPException(status_code=400, detail="Server ID mismatch")
    tickets[ticket.ticket_id] = ticket
    return ticket

@app.get("/servers/{server_id}/tickets/{ticket_id}")
async def get_ticket(server_id: str, ticket_id: str):
    if ticket_id not in tickets or tickets[ticket_id].server_id != server_id:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return tickets[ticket_id]

@app.get("/servers/{server_id}/knowledge_base")
async def list_knowledge_base_articles(server_id: str):
    return [article for article in knowledge_base.values() if article.server_id == server_id]


@app.post("/servers/{server_id}/knowledge_base", response_model=KnowledgeBaseArticle)
async def create_knowledge_base_article(server_id: str, article: KnowledgeBaseArticle):
   if article.server_id != server_id:
        raise HTTPException(status_code=400, detail="Server ID mismatch")
   knowledge_base[article.article_id] = article
   return article

@app.get("/servers/{server_id}/knowledge_base/{article_id}")
async def get_knowledge_base_article(server_id: str, article_id: str):
    if article_id not in knowledge_base or knowledge_base[article_id].server_id != server_id:
        raise HTTPException(status_code=404, detail="Article not found")
    return knowledge_base[article_id]
