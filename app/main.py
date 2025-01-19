from fastapi import FastAPI, HTTPException
from enum import Enum

app = FastAPI()


class GenreURLChoices(Enum):
	"""
	GenreURLChoices is Enum type which allows user to
	select data from given specific type
	"""

	ROCK = 'rock'
	ELECTRONIC = 'electronic'
	METAL = 'metal'
	HIP_HOP = 'hip-hop'


BANDS = [
	{"id": 1, "name": "Led Zeppelin", "genre": "Rock"},
	{"id": 2, "name": "Pink Floyd", "genre": "Electronic"},
	{"id": 3, "name": "Queen", "genre": "Rock"},
	{"id": 4, "name": "Metallica", "genre": "Hip Hop"},
	{"id": 5, "name": "AC/DC", "genre": "Metal"},
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


@app.get("/bands/genre/{genre}")
async def bands_for_genre(genre: GenreURLChoices) -> list[dict]:
	return [
		b for b in BANDS if b['genre'].lower() == genre.value
	]
