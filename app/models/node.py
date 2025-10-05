
from pydantic import BaseModel
from typing import List

class Node(BaseModel):
	id: int
	title: str
	abstract: str
	reference: str
	authors: str
	data: str
	link: str

class NodeList(BaseModel):
    nodes: List[Node]






