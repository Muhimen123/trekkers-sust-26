- Create a virtual environement 

```bash
python -m venv .venv
```
- Install all the requirements 

```bash 
pip3 install -r requirements.txt
```

- Run the API 
```bash 
uvicorn app.main:app --reload
```

- Open the following link in your browser

http://127.0.0.1:8000/docs