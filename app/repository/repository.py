import json
import pandas as pd
from models.node import Node
from models.edge import Edge

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

        node = Node()

        node.id = id
        node.name = article['title']
        node.abstract = article['abstract']
        node.embedding = article['embedding']

        return node

    except Exception as e:
        print(f"ERROR: {e}")
        return None


if __name__ == '__main__':
    convert_csv_to_json('app/utils/artigos_embeddings.csv', 'app/repository/data.json')