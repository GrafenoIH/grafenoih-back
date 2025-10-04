from pydantic import BaseModel
from typing import List
from app.models.node import Node

class Edge(BaseModel):
    source: Node
    target: Node
    type: str
    weight: float

class EdgeList(BaseModel):
    edges: List[Edge]
