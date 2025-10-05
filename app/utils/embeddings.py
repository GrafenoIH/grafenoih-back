import numpy as np
import pandas as pd
import json
from typing import List

class EmbeddingEngine:
    def __init__(self, vocab_size=1000):
        self.vocab_size = vocab_size
        
    def _create_vocabulary(self, text: str) -> dict:
        """Creates a simple word-to-index mapping"""
        words = text.lower().split()
        return {word: i for i, word in enumerate(set(words))}

    def text_to_embedding(self, text: str) -> np.ndarray:
        """Convert text to a simple bag-of-words embedding"""
        words = text.lower().split()
        embedding = np.zeros(self.vocab_size)
        for word in words:
            # Using hash to get consistent index for words
            index = hash(word) % self.vocab_size
            embedding[index] += 1
        # Normalize the vector
        norm = np.linalg.norm(embedding)
        return embedding / norm if norm > 0 else embedding

    def compare_embeddings(self, embedding1: np.ndarray, embedding2: np.ndarray) -> float:
        # Existing implementation is good, no changes needed
        norm1 = np.linalg.norm(embedding1)
        norm2 = np.linalg.norm(embedding2)
        if norm1 == 0 or norm2 == 0:
            return 0.0
        return np.dot(embedding1, embedding2) / (norm1 * norm2)

    def batch_encode(self, texts: List[str]) -> np.ndarray:
        """Encode multiple texts at once"""
        embeddings = np.zeros((len(texts), self.vocab_size))
        for i, text in enumerate(texts):
            embeddings[i] = self.text_to_embedding(text)
        return embeddings

    # Rest of the methods remain the same
    def read_csv(self, csv_path: str, text_column: str) -> np.ndarray:
        try:
            df = pd.read_csv(csv_path)
            texts = df[text_column].tolist()
            embeddings = self.batch_encode(texts)
            return embeddings
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
    
    return similarity

def export_json(file_name: str, matrix: list):
    with open(f'{file_name}', 'w') as f:
        json.dump(matrix, f)


if __name__ == "__main__":
    engine = EmbeddingEngine()
    path = 'app/utils/artigos_embeddings.csv'

    s = calculate_similarity(path, engine)
    export_json('similarity.json', s)
