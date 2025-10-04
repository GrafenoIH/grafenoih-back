# grafenoIH

## Passo a passo para iniciar o projeto

1. **Clone o repositório**

   ```powershell
   git clone <URL-do-repositório>
   cd grafenoIH
   ```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado)**

   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Instale as dependências**

   ```powershell
   pip install -r requirements.txt
   ```

4. **Instale o FastAPI (caso não esteja no requirements.txt)**

   ```powershell
   pip install "fastapi[standard]"
   pip install uvicorn
   ```

5. **Execute o servidor**

   ```powershell
   uvicorn main:app --reload
   ```

6. **Acesse o projeto**
   Abra o navegador e acesse: [http://localhost:8000](http://localhost:8000)

7. **Documentação automática**
   Acesse [http://localhost:8000/docs](http://localhost:8000/docs) para ver a documentação interativa da API.

---

### Observações

- Certifique-se de que o arquivo `main.py` possui uma instância chamada `app` do FastAPI.
- O arquivo `requirements.txt` pode ser gerado com:
  ```powershell
  pip freeze > requirements.txt
  ```
- Para dúvidas, consulte a [documentação do FastAPI](https://fastapi.tiangolo.com/).
