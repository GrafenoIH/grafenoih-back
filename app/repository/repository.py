import json
import pandas as pd
from app.models.node import Node
from app.models.edge import Edge

def read_similarity_matrix(file_name: str):
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            matrix = json.load(f)

        return matrix

    except Exception as e:
        print(f'ERROR: {e}')
    return None


def convert_csv_to_json(csv_path: str, json_path: str):
    try:
        df = pd.read_csv(csv_path, encoding='utf-8')

        df = df.iloc[:, 2:]

        df.to_json(json_path, orient='records', indent=4, force_ascii=False)

    except Exception as e:
        print(f"ERROR: {e}")


def create_node(json_path: str, id: int):
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        article = data[id]

        node = Node(
            id = id,
            title = article["title"],
            abstract = article["abstract"],
            reference = article["references"],
            authors = article["authors"],
            data = article["date"],
            link = article["link"],
        )

        return node

    except Exception as e:
        print(f"ERROR: {e}")
        return None

def create_edge(json_path: str, id1: int, id2: int):
    try:
        edge = Edge(
            source= id1,
            target= id2,
            similarity= compare_edges(json_path, id1, id2),
            isReference= False,
        )
        
        return edge

    except Exception as e:
        print(f"ERROR: {e}")
        return None

def compare_edges(json_path: str, id: int, id2: int):
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

            edge_similarity = data[id]["similarity"][id2]

            return edge_similarity

    except Exception as e:
        print(f"ERROR: {e}")
        return None
    


def read_json(path: str):
    with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    return data

def create_edges_json(path_nodes: str, path_similarity: str, path_return: str):
    i = 0
    data_json = read_json(path_nodes)
    similarity = read_json(path_similarity)
    for a in data_json:
        a["similarity"] = similarity[i]
        i = i + 1
    
    with open(path_return, 'w', encoding='utf-8') as f:
        json.dump(data_json, f, ensure_ascii=False, indent=4)

# if __name__ == '__main__':
#    convert_csv_to_json('app/utils/artigos_embeddings.csv', 'app/repository/data.json')

#    a = "app/repository/data.json"
#    b = "app/repository/similarity.json"

#    create_edges(a, b, "data2.json")

    # print(create_edges("data2.json", 120, 320))   