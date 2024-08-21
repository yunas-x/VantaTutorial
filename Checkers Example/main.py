from typing import Annotated, Union
from fastapi import FastAPI, Header, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from Board import three_x_three_board
from Log import log

app = FastAPI(summary="Demo",
              description="Demo for Vanta",
              version="1.0.0")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

board = three_x_three_board()

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.get("/board", response_class=HTMLResponse)
async def index(request: Request, hx_request: Annotated[Union[str, None], Header()] = None):
    if hx_request:
        return templates.TemplateResponse(
            request=request, name="board.html", context={"board": board, "highlighted": []}
        )
    return JSONResponse(content=jsonable_encoder(board))

@app.get("/board/{coord_x}/{coord_y}", response_class=HTMLResponse)
async def index(coord_x: int, coord_y: int, request: Request, hx_request: Annotated[Union[str, None], Header()] = None):

    current_cell = board.cell_with(coord_x=coord_x, coord_y=coord_y)
    previous_cell = log.pop() if log else None

    if board.move(previous_cell, current_cell):
        cells_to_move = []
    else:
        log.append(current_cell)
        cells_to_move = board.can_move_from(cell=current_cell)


    if hx_request:
        return templates.TemplateResponse(
            request=request, name="board.html", context={"board": board, "highlighted": cells_to_move}
        )
    return JSONResponse(content=jsonable_encoder(board))