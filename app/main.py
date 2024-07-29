import os

import aiohttp
import asyncio
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from .api import *
from .parsers_data import *
from .brands import brands

app = FastAPI()

templates = Jinja2Templates(
    directory=os.path.join(os.path.dirname(__file__), 'templates')
)

app.mount('/static', StaticFiles(
    directory=os.path.join(os.path.dirname(__file__), 'static')),
    name='static'
)


@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    article = request.query_params.get('article')
    brand = request.query_params.get('brand')

    if not article:
        return templates.TemplateResponse(
            'base.html', context={
                'request': request,
                'all_brands': brands,
            }
        )

    async with aiohttp.ClientSession() as session:
        tasks = [
            favorit_get_method(session, article, brand),
            forum_get_method(session, article, brand),
            moskvorechie_get_method(session, article, brand),
            armtek_get_method(session, article, brand),
            profitliga_get_method(session, article),
            autoeuro_get_method(session, article, brand),
            rossko_get_method(article, brand),
            mikado_get_method(session, article, brand),
            motex_get_method(session, article, brand),
        ]
        result = await asyncio.gather(*tasks)
        favorit, forum, msk, armtek, profit, ae, rossko, mikado, motex = result
        pars_task = [
            favorit_pars(favorit),
            forum_pars(forum),
            moskvorechie_pars(msk),
            armtek_pars(armtek),
            profitliga_pars(profit),
            autoeuro_pars(ae),
            rossko_pars(rossko),
            mikado_parts(mikado),
            motex_parts(motex),
        ]
        pars_result = await asyncio.gather(*pars_task)
        result_data = [item for sublist in pars_result for item in sublist]
        result_data.sort(key=lambda x: x['price'])
        return templates.TemplateResponse(
            'base.html', context={
                'request': request,
                'all_brands': brands,
                'data': result_data,
            }
        )
