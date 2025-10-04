

from app.models.edge import Edge, EdgeList
from app.models.node import Node, NodeList
from fastapi import HTTPException


node1 = Node(id=1, name="Node 1", abstract="First node", embedding=[0.1, 0.2, 0.3])
node2 = Node(id=2, name="Node 2", abstract="Second node", embedding=[0.4, 0.5, 0.6])
node3 = Node(id=3, name="Node 3", abstract="Third node", embedding=[0.7, 0.8, 0.9])

nodes_data = [node1, node2, node3]

edges_data = [
	Edge(id=1, source=node1, target=node2, type=True, weight=1.0),
	Edge(id=2, source=node2, target=node3, type=False, weight=2.5),
	Edge(id=3, source=node3, target=node1, type=True, weight=0.75)
]

def get_edge_by_id(edge_id: int) -> Edge:
	try:
		for edge in edges_data:
			if edge.id == edge_id:
				return edge
		raise HTTPException(status_code=404, detail=f"Edge with id {edge_id} not found")
	except Exception as e:
		raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")

def get_all_edges() -> EdgeList:
	try:
		if not edges_data:
			raise HTTPException(status_code=404, detail="No edges found")
		return EdgeList(edges=edges_data)
	except Exception as e:
		raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")

def get_node_by_id(node_id: int) -> Node:
	try:
		for node in nodes_data:
			if node.id == node_id:
				return node
		raise HTTPException(status_code=404, detail=f"Node with id {node_id} not found")
	except Exception as e:
		raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")

def get_all_nodes() -> NodeList:
	try:
		if not nodes_data:
			raise HTTPException(status_code=404, detail="No nodes found")
		return NodeList(nodes=nodes_data)
	except Exception as e:
		raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")