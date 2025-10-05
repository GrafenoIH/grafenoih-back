
from fastapi import APIRouter, HTTPException
from app.services.graph_service import edge_generator, get_all_edges, get_node_by_id, node_generator, search_nodes_by_title
from app.models.edge import EdgeList
from app.models.node import NodeList, Node
from fastapi.responses import StreamingResponse

router = APIRouter()

@router.get("/edges", response_model=EdgeList)
def read_all_edges():
	return get_all_edges()

@router.get("/edges/stream")
def stream_edges():
    return StreamingResponse(edge_generator(), media_type="application/x-ndjson")

@router.get("/nodes/stream")
def read_all_nodes():
	return StreamingResponse(node_generator(), media_type="application/x-ndjson")

@router.get("/node/{node_id}", response_model=Node)
def read_node(node_id: int):
	node = get_node_by_id(node_id)
	if node is None:
		raise HTTPException(status_code=404, detail="Node not found")
	return node

@router.get("/nodes/search/{title}", response_model=NodeList)
def search_node(title: str):
	nodes = search_nodes_by_title(title)
	return nodes

@router.get("/health")
def health_check():
	return {"status": "ok"}