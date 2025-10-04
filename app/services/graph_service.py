
from app.models.edge import Edge, EdgeList
from app.models.node import Node


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
	if 0 <= edge_id < len(edges_data):
		return edges_data[edge_id]
	return None

def get_all_edges() -> EdgeList:
	return EdgeList(edges=edges_data)

def get_node_by_id(node_id: int) -> Edge:
	if 0 <= node_id < len(nodes_data):
		return edges_data[node_id]
	return None

def get_all_nodes() -> EdgeList:
	return EdgeList(edges=nodes_data)