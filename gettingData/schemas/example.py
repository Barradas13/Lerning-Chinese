from pydantic import BaseModel, Field

class Character(BaseModel):
    char: str = Field(description="单个汉字")
    pinyin: str = Field(description="带声调的拼音")
    meaning: str = Field(description="英文释义")

class Lesson(BaseModel):
    id: int = Field(description="课号")
    title: str = Field(description="课名")
    characters: list[Character] = Field(description="本课所有汉字")

class Schema(BaseModel):
    lessons: list[Lesson] = Field(description="全书所有课")