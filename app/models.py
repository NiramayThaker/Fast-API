from enum import Enum
from typing import Optional
from pydantic import BaseModel, validator
from sqlmodel import SQLModel, Field, Relationship
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


class AlbumBase(SQLModel):
	title: str
	release_date: date
	band_id: int = Field(foreign_key="band.id")


class Album(AlbumBase, table=True):
	id: int = Field(default=None, primary_key=True)
	band: "Band" = Relationship(back_populates="albums")


class BandBase(SQLModel):
	name: str
	genre: GenreChoices


class BandCreate(BandBase, table=True):
	"""
	Schema for post request for creating new band
	"""
	
	albums: Optional[list[AlbumBase]] = None

	@validator('genre', pre=True)
	def title_case_genre(cls, value):
		return value.title()


class Band(BandBase, table=True):
	id: int = Field(default=None, primary_key = True)
	albums: list[Album] = Relationship(back_populates="band")
