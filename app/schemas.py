from enum import Enum
from pydantic import BaseModel, validator
from datetime import date


class GenreURLChoices(Enum):
	"""
	GenreURLChoices is Enum type which allows user to
	select data from given specific type
	"""

	ROCK = 'rock'
	ELECTRONIC = 'electronic'
	METAL = 'metal'
	HIP_HOP = 'hip-hop'


class GenreChoices(Enum):
	ROCK = 'rock'
	ELECTRONIC = 'rlectronic'
	METAL = 'metal'
	HIP_HOP = 'hip-hop'


class Album(BaseModel):
	title: str
	release_date: date


class BandBase(BaseModel):
	name: str
	genre: GenreChoices
	albums: list[Album] = []


class BandCreate(BandBase):
	@validator('genre', pre=True)
	def title_case_genre(cls, value):
		return value.title()


class BandWithId(BandBase):
	id: int
