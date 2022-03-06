from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def root():
    return {'status': 'fine'}


@app.get('/{word}')
def word(word: str):
    return {'message': f'{word}'}
