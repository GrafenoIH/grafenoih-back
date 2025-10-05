from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import json

class EmbeddingEngine:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)


    def text_to_embedding(self, text: str) -> np.ndarray:
        return self.model.encode(text, convert_to_numpy=True)


    def compare_embeddings(self, embedding1: np.ndarray, embedding2: np.ndarray) -> float:
        return cosine_similarity([embedding1], [embedding2])[0][0]


    def batch_encode(self, texts: list) -> np.ndarray:
        return self.model.encode(texts, convert_to_numpy=True, show_progress_bar=True)


    def read_csv(self, csv_path: str, text_column: str) ->tuple:
        try:
            df = pd.read_csv(csv_path)
            texts = df[text_column].tolist()
            embeddings = self.batch_encode(texts)
            
            return  embeddings

        except Exception as e:
            raise Exception(e)
        
    def calculate_embeddings(self, row: pd.core.series.Series, text_column: str):
        try:
            abstract = row[text_column]
            emb = self.text_to_embedding(abstract)
            return emb
        except Exception as e:
            print(f'ERROR: {e}')
            return [0]

def string_to_array(s):
    s = s.strip()[1:-1]

    str_numbers = filter(None, s.split(' '))

    return np.array([float(num) for num in str_numbers])

def calculate_similarity(csv_path: str ,engine: EmbeddingEngine) -> list:
    df = pd.read_csv(csv_path)

    df['embedding'] = df['embedding'].apply(string_to_array)

    n = len(df)

    similarity = [[0 for _ in range(n)] for _ in range(n)]

    for i1, row1 in df.iterrows():
        for i2, row2 in df.iterrows():
            if i1 > i2: 
                continue
            
            sim = engine.compare_embeddings(row1['embedding'], row2['embedding'])
            similarity[i1][i2] = sim
            similarity[i2][i1] = sim
    
    return similarity

def export_json(file_name: str, matrix: list):
    with open(f'app/utils/{file_name}', 'w') as f:
        json.dump(matrix, f)


if __name__ == "__main__":
    engine = EmbeddingEngine()
    path = 'app/utils/artigos_embeddings.csv'

    s = calculate_similarity(path, engine)
    export_json('app/utils/similarity.json', s)
