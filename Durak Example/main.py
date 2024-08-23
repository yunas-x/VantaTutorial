from typing import Annotated, Union
from fastapi import FastAPI, Header, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

from random import randint

from Trash import the_hand, the_deck

app = FastAPI(summary="Demo",
              description="Demo for Vanta",
              version="1.0.0")

templates = Jinja2Templates(directory="templates")

@app.get("/1", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(request=request, name="index1.html")

@app.get("/2", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(request=request, name="index2.html")

@app.get("/cards/1", response_class=HTMLResponse)
def get_cards(request: Request, hx_request: Annotated[Union[str, None], Header()] = None):

    card = the_deck.pop()
    the_hand.cards.append(card)

    return templates.TemplateResponse(request=request, name="button.html")


@app.get("/cards/2", response_class=HTMLResponse)
def get_cards(request: Request, hx_request: Annotated[Union[str, None], Header()] = None):

    if hx_request:
        return templates.TemplateResponse(
            request=request, name="cards.html", context={"hand": the_hand}
        )
    return JSONResponse(content=jsonable_encoder(the_hand.cards))
