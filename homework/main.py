from typing import List
from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy.future import select

import models
import schemas
from database import engine, session


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)
    yield
    await session.close()
    await engine.dispose()


app = FastAPI(lifespan=lifespan)


@app.post('/recipes/', response_model=schemas.RecipeOut)
async def recipes(recipe: schemas.RecipeIn) -> models.Recipe:
    new_recipe = models.Recipe(**recipe.dict())
    async with session.begin():
        session.add(new_recipe)
    return new_recipe


@app.get('/recipes/', response_model=List[schemas.AllRecipeOut])
async def recipes() -> List[models.Recipe]:
    res = await session.execute(select(models.Recipe).order_by(models.Recipe.views.desc(),
                                                               models.Recipe.time_to_cook.asc()))
    return res.scalars().all()

@app.get('/recipes/{recipe_id}', response_model=schemas.RecipeOut)
async def recipes(recipe_id) -> List[models.Recipe]:
    recipe = await session.get(models.Recipe, recipe_id)
    recipe.views += 1
    await session.commit()
    return recipe