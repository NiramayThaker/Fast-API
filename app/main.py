from typing import Optional, Annotated
from fastapi import FastAPI, HTTPException, Path, Query
from app.models import GenreURLChoices, BandCreate, Band, Album

app = FastAPI()

BANDS = [
    {
        "id": 1,
        "name": "Led Zeppelin",
        "genre": "rock",
        "albums": [],
    },
    {
        "id": 2,
        "name": "Pink Floyd",
        "genre": "rock",
        "albums": [
            {"title": "Wish You Were Here", "release_date": "1975-09-12"},
        ],
    },
    {
        "id": 3,
        "name": "The Beatles",
        "genre": "rock",
        "albums": [
            {"title": "Abbey Road", "release_date": "1969-09-26"},
        ],
    },
    {
        "id": 4,
        "name": "Metallica",
        "genre": "metal",
        "albums": [
            {"title": "Kill 'Em All", "release_date": "1983-07-25"},
            {"title": "Ride the Lightning", "release_date": "1984-07-27"},
            {"title": "The Black Album", "release_date": "1991-08-12"},
        ],
    },
    {
        "id": 5,
        "name": "AC/DC",
        "genre": "rock",
        "albums": [
            {"title": "High Voltage", "release_date": "1976-04-30"},
        ],
    },
    {
        "id": 6,
        "name": "Nirvana",
        "genre": "rock",
        "albums": [
            {"title": "Bleach", "release_date": "1989-06-15"},
            {"title": "Nevermind", "release_date": "1991-09-24"},
            {"title": "In Utero", "release_date": "1993-09-21"},
            {"title": "MTV Unplugged in New York", "release_date": "1994-11-01"},
        ],
    },
]



# @app.get("/bands")
# async def bands(
#     genre: Optional[GenreURLChoices] = None,
#     q: Annotated[Optional[str], Query(max_length=10)] = None
# ) -> list[BandWithId]:
#     """
#     Making query parameter optional (it can accept None)
#     Also gets default behavior of GenreURLChoices for data filtering
#     """
#     band_list = [BandWithId(**b) for b in BANDS]

#     if genre:
#         band_list = [
#             b for b in band_list if b.genre.value.lower() == genre.value.lower()
#         ]

#     if q:
#         band_list = [b for b in band_list if q.lower() in b.name.lower()]

#     return band_list


# @app.get("/bands/{band_id}")
# async def get_bands(band_id: Annotated[int, Path(title="The band ID")]) -> BandWithId:
# 	bands = next((BandWithId(**b) for b in BANDS if b['id'] == band_id), None)
# 	if bands is None:
# 		raise HTTPException(status_code=404, detail='Band not found')

# 	return bands


# @app.get("/bands/genre/{genre}")
# async def bands_for_genre(genre: GenreURLChoices) -> list[dict]:
# 	return [
# 		b for b in BANDS if b['genre'].lower() == genre.value
# 	]


# @app.post("/bands")
# async def create_band(band_data: BandCreate) -> BandWithId:
# 	id = BANDS[-1]['id'] + 1
# 	band = BandWithId(id=id, **band_data.model_dump()).model_dump()
# 	BANDS.append(band)

# 	return band


