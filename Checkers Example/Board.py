from Cell import Cell

class Board:

    def __init__(self, cells: list[Cell]) -> None:
        self.cells = cells
    
    def can_move_from(self, cell: Cell) -> list[Cell]:
        return [c for c in self.cells if c.reacheable_from(cell)]
    
    def cell_with(self, coord_x: int, coord_y: int) -> Cell:
        selection = [c for c in self.cells if c.coord_x == coord_x and c.coord_y == coord_y]
        return selection[0]

def three_x_three_board() -> Board:
    cells = [
        Cell(coord_x=1, coord_y=1, is_occupied=True), Cell(coord_x=3, coord_y=1, is_occupied=False),
        Cell(coord_x=2, coord_y=2, is_occupied=True),
        Cell(coord_x=1, coord_y=3, is_occupied=True), Cell(coord_x=3, coord_y=3, is_occupied=False),
    ]
    return Board(cells=cells)
    