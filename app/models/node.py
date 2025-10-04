
from pydantic import BaseModel
from typing import List

class Node(BaseModel):
	id: int
	name: str
	abstract: str
	embedding: List[float]

class NodeList(BaseModel):
    nodes: List[Node]






