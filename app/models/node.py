
from pydantic import BaseModel
from typing import List

class IdData(BaseModel):
	name: str
	abstract: str
	embedding: List[float]

class Node(BaseModel):
	id: IdData




