from fastapi import FastAPI, HTTPException

app = FastAPI()

BANDS = [
	{"id": 1, "name": "Led Zeppelin", "genre": "Rock"},
	{"id": 2, "name": "Pink Floyd", "genre": "Progressive Rock"},
	{"id": 3, "name": "The Beatles", "genre": "Pop Rock"},
	{"id": 4, "name": "Metallica", "genre": "Heavy Metal"},
	{"id": 5, "name": "AC/DC", "genre": "Hard Rock"},
	{"id": 6, "name": "Nirvana", "genre": "Grunge"},
	{"id": 7, "name": "Queen", "genre": "Rock"},
	{"id": 8, "name": "Coldplay", "genre": "Alternative Rock"},
	{"id": 9, "name": "Green Day", "genre": "Punk Rock"}
]


@app.get("/bands")
async def read_root() -> list[dict]:
	return BANDS


@app.get("/bands/{band_id}")
async def read_root(band_id: int) -> dict:
	bands = next((b for b in BANDS if b['id'] == band_id), None)
	if bands is None:
		raise HTTPException(status_code=404, detail='Band not found')

	return bands
