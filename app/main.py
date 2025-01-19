from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root() -> dict[str, str]:
	return {"Hello": "World!"}


@app.get('/about')
async def about() -> str:
	return 'About section of company'
