from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import ast

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


def safe_embedding_converter(value):
    if isinstance(value, str):
        try:
            return np.array(ast.literal_eval(value))
        except (ValueError, SyntaxError):
            print(f'Erro no valor: {value}')
            return np.array([0.0])
    else:
        return np.array([value])

def calculate_similarity(csv_path: str ,engine: EmbeddingEngine) -> list:
    df = pd.read_csv(csv_path)

    df['embedding'] = df['embedding'].apply(safe_embedding_converter)

    n = len(df)
    similarity = [[0 for _ in range(n)] for _ in range(n)]

    for i1, row1 in df.iterrows():
        for i2, row2 in df.iterrows():
            
            sim = engine.compare_embeddings(row1['embedding'], row2['embedding'])
            similarity[i1][i2] = sim
            similarity[i2][i1] = sim
    
    return similarity


if __name__ == "__main__":
    # embeddings = engine.read_csv('app/utils/test_publications.csv', 'Abstract')
    # similarity = engine.compare_embeddings(embeddings[1], embeddings[2])
    # print(embeddings[1], embeddings[2])
    # print(f"Similaridade: {similarity:.4f}")
    # df = pd.read_csv('app/utils/artigos.csv')
    # df['embeddings'] = [[] for _ in range(len(df))]
    # df['embeddings'] = df['embeddings'].astype(object)
    # engine = EmbeddingEngine()
    # for i, r in df.iterrows():
    #     if i == 5:
    #         break
    #     emb = engine.calculate_embeddings(r, 'abstract')
    #     df.at[i, 'embeddings'] = emb
    #     # print(type(r))  
    # print(df['embeddings'].head())
    engine = EmbeddingEngine()
    s = calculate_similarity('app/utils/artigos_embeddings.csv', engine)
    for i in range(5):
        print(s[i])