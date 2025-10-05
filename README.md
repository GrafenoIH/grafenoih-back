# grafenoIH

## Step-by-step to start the project

1. **Clone the repository**

   ```powershell
   git clone <repository-URL>
   cd grafenoIH
   ```

2. **Create and activate a virtual environment (optional but recommended)**

   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install dependencies**

   ```powershell
   pip install -r requirements.txt
   ```

4. **Install FastAPI (if not in requirements.txt)**

   ```powershell
   pip install "fastapi[standard]"
   pip install uvicorn
   ```

5. **Run the server**

   ```powershell
   uvicorn main:app --reload
   ```

6. **Access the project**
   Open your browser and go to: [http://localhost:8000](http://localhost:8000)

7. **Automatic documentation**
   Go to [http://localhost:8000/docs](http://localhost:8000/docs) to see the interactive API documentation.

8. **Build Docker**
   run:
   ```powershell
   docker build -t grafenoih-api .
   ```

   ```powershell
   docker run -d -p 8000:8000 --name grafenoih-container grafenoih-api
   ```

---

### Notes

- Make sure the `main.py` file has an instance called `app` from FastAPI.
- You can generate the `requirements.txt` file with:
  ```powershell
  pip freeze > requirements.txt
  ```
- For questions, check the [FastAPI documentation](https://fastapi.tiangolo.com/).
