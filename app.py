from fastapi import FastAPI
import uvicorn

app = FastAPI(title='Modern Hello World')

@app.get('/')
def read_root():
    return {
        'message': 'Hello World',
        'status': 'Modern & Functional',
        'platform': 'PowerShell Automated'
    }

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
