from Cell import Cell

class Board:

    def __init__(self, cells: list[Cell]) -> None:
        self.cells = cells
    
    def can_move_from(self, cell: Cell) -> list[Cell]:
        return [c for c in self.cells if c.reacheable_from(cell)]
    
    def cell_with(self, coord_x: int, coord_y: int) -> Cell:
        selection = [c for c in self.cells if c.coord_x == coord_x and c.coord_y == coord_y]
        return selection[0]
    
    def move(self, cell_from: Cell, cell_to: Cell) -> bool:
        # тут еще должна проверка на рубку шашки врага
        if cell_from and cell_to in self.can_move_from(cell_from):
            cell_from.is_occupied = False
            cell_to.is_occupied = True
            return True
        else:
            return False

def three_x_three_board() -> Board:
    cells = []
    for i in range(1, 9):
        for j in range(1, 9):
            if i < 4:
                cells.append(Cell(coord_x=i, coord_y=j, is_occupied=True))
            else:
                cells.append(Cell(coord_x=i, coord_y=j, is_occupied=False))

    return Board(cells=cells)
    