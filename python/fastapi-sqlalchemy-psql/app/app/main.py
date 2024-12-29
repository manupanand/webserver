from fastapi import FastAPI


app: FastAPI= FastAPI(
    title="Note API using FAST API",
    description="This is a simple REST API built with postgres",
    docs_url="/"
)
#define here to give specifics to swagger ui for openapi spec



@app.get('/notes')
async def get_all_notes():
    pass


@app.post('/notes')
async def create_nore():
    pass

@app.get('/note/{note_id}')
async def get_note_by_id(note_id):
    pass

@app.patch('/note/{note_id}')
async def update_note(note_id):
    pass

@app.delete('/note/{note_id}')
async def delete_note(note_id):
    pass