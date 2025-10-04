from pydantic import BaseModel
from typing import List
from app.models.node import Node

class Edge(BaseModel):
    id: int
    source: Node
    target: Node
    type: bool
    weight: float

class EdgeList(BaseModel):
    edges: List[Edge]
