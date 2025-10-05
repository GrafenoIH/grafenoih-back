from pydantic import BaseModel
from typing import List
from app.models.node import Node

class Edge(BaseModel):
    source: int
    target: int
    isReference: bool
    similarity: float

class EdgeList(BaseModel):
    edges: List[Edge]
