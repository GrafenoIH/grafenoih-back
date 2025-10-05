
from functools import lru_cache
from app.models.edge import Edge, EdgeList
from app.models.node import Node, NodeList
from app.repository.repository import read_json, create_node, create_edge, compare_edges
from fastapi import HTTPException
import json

nodes = []

nodes_data = []

edges_data = [

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
		edges = []
		json = read_json("similarity.json")
		count = 0
		for i in range(len(json)):
			for j in range(len(json[i])):
				id1 = i
				id2 = j
				similarity = json[i][j]
				if similarity < 0:
					continue
				count += 1
				edge = Edge(
					source=id1,
					target=id2,
					isReference=False,
					similarity=similarity
				)
				edges.append(edge)
		print(count)
		return EdgeList(edges=[])
			
			


	except Exception as e:
		raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")

def edge_generator():
    json_data = read_json("similarity.json")
    for i in range(len(json_data)):
        for j in range(len(json_data[i])):
            if json_data[i][j] < 0.5:
               continue
            edge = {
                "source": i,
                "target": j,
                "isReference": False,
                "similarity": json_data[i][j]
            }
            yield json.dumps(edge) + "\n"

def get_node_by_id(node_id: int) -> Node:
	try:
		for node in nodes_data:
			if node.id == node_id:
				return node
		raise HTTPException(status_code=404, detail=f"Node with id {node_id} not found")
	except Exception as e:
		raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")

# @lru_cache(maxsize=None)
def get_all_nodes():
	try:
		nodes_json = read_json("data.json")
		nodes = []
		for i in range(len(nodes_json)) :
			node = create_node("data.json", i)
			nodes.append(node)
		
		return nodes

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