from typing import Annotated, Union
from fastapi import FastAPI, Header, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from Board import three_x_three_board

app = FastAPI(summary="Demo",
              description="Demo for Vanta",
              version="1.0.0")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

board = three_x_three_board()
selected_cell = None

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

    # Selected cell
    cell = board.cell_with(coord_x=coord_x, coord_y=coord_y)

    # If occupied evaluate the cells where we can go
    if cell.is_occupied:
        cells_to_move = board.can_move_from(cell=cell)
    else:
        cells_to_move = []


    if selected_cell is None and cells_to_move:
        selected_cell == cell

    # if selected_cell is not None and cell in cells_to_move:
    #   move_figure()
    # if selected_cell is not None and cell not in cells_to_move
    #   dont_move_figure()
    # if selected_cell is None and not cells_to_move
    #   ignore()

    if hx_request:
        return templates.TemplateResponse(
            request=request, name="board.html", context={"board": board, "highlighted": cells_to_move}
        )
    return JSONResponse(content=jsonable_encoder(board))