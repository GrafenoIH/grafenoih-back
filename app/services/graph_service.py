

from app.models.edge import Edge, EdgeList
from app.models.node import Node, NodeList
from fastapi import HTTPException


node1 = Node(id=1, name="Gabryel", abstract="First node", embedding=[0.1, 0.2, 0.3])
node2 = Node(id=2, name="Guilherme", abstract="Second node", embedding=[0.4, 0.5, 0.6])
node3 = Node(id=3, name="Lucas", abstract="Third node", embedding=[0.7, 0.8, 0.9])

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
	
def search_nodes_by_title(title: str, max_distance: int = 8) -> NodeList:
    try:
        matched_nodes = [
            node for node in nodes_data
            if levenshtein(node.name.lower(), title.lower()) <= max_distance
        ]
        if not matched_nodes:
            raise HTTPException(status_code=404, detail="No nodes found with similar title")
        return NodeList(nodes=matched_nodes)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")
	


def levenshtein(a: str, b: str) -> int:
    if len(a) < len(b):
        return levenshtein(b, a)
    if len(b) == 0:
        return len(a)
    previous_row = range(len(b) + 1)
    for i, c1 in enumerate(a):
        current_row = [i + 1]
        for j, c2 in enumerate(b):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]