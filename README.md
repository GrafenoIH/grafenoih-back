# grafeno

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

3. **Build Docker**
   run:

   ```powershell
   docker build -t grafenoih-api .
   ```

   ```powershell
   docker run -d -p 8000:8000 --name grafenoih-container grafenoih-api
   ```

4. **Access the project**
   Open your browser and go to: [http://localhost:8000](http://localhost:8000)

---

5. **Automatic documentation**
   Go to [http://localhost:8000/docs](http://localhost:8000/docs) to see the interactive API documentation.

### Notes

- Make sure the `main.py` file has an instance called `app` from FastAPI.
- You can generate the `requirements.txt` file with:
  ```powershell
  pip freeze > requirements.txt
  ```
- For questions, check the [FastAPI documentation](https://fastapi.tiangolo.com/).

### Used libraries

[FastAPI documentation](https://fastapi.tiangolo.com/).
[Pandas documentation](https://pandas.pydata.org/docs/).
[Pydantic documentation](https://docs.pydantic.dev/latest/api/base_model/).
[Functools documentation](https://docs.python.org/3/library/functools.html).

## License

This project is licensed under the **MIT License** -
