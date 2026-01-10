from pydantic import BaseModel


class BaseRecipe(BaseModel):
    name: str
    time_to_cook: int


class RecipeIn(BaseRecipe):
    title: str
    ingredients: str

class AllRecipeOut(BaseRecipe):
    views: int

    class Config:
        orm_mode = True

class RecipeOut(BaseRecipe):
    ingredients: str
    title: str

    class Config:
        orm_mode = True