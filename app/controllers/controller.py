
from fastapi import APIRouter, HTTPException
from app.services.graph_service import get_edge_by_id, get_all_edges, get_all_nodes, get_node_by_id, search_nodes_by_title
from app.models.edge import EdgeList, Edge
from app.models.node import NodeList, Node


router = APIRouter()

@router.get("/edges", response_model=EdgeList)
def read_all_edges():
	return get_all_edges()

@router.get("/edges/{edge_id}", response_model=Edge)
def read_edge(edge_id: int):
	edge = get_edge_by_id(edge_id)
	if edge is None:
		raise HTTPException(status_code=404, detail="Node not found")
	return edge

@router.get("/nodes")
def read_all_nodes():
	return get_all_nodes()

@router.get("/nodes/{node_id}", response_model=Node)
def read_node(node_id: int):
	node = get_node_by_id(node_id)
	if node is None:
		raise HTTPException(status_code=404, detail="Node not found")
	return node

@router.get("/nodes/search/{title}", response_model=NodeList)
def search_node(title: str):
	nodes = search_nodes_by_title(title)
	return nodes
