# pip install FastApi

from typing import Annotated, Union
from fastapi import FastAPI, Header, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

from Hand import Hand, the_hand

app = FastAPI(summary="Demo",
              description="Demo for Vanta",
              version="1.1.0")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):

    global the_hand
    the_hand = Hand()

    return templates.TemplateResponse(request=request, name="index.html")

@app.get("/cards", response_class=HTMLResponse)
async def get_cards(request: Request, hx_request: Annotated[Union[str, None], Header()] = None):

    global the_hand
    if not the_hand:
        the_hand = Hand()
    the_hand.add_card()

    if hx_request:
        return templates.TemplateResponse(
            request=request, name="cards.html", context={"hand": the_hand}
        )
    return JSONResponse(content=jsonable_encoder(the_hand.cards))