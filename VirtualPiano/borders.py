import pygame as pg
from shapes import RectangleShape
from config import BORDER_W
from colors import BLACK


class RectangleBorder(RectangleShape):  
    def __init__(self,
                 sizes: tuple[int, int],
                 pos: tuple[int, int],
                 line_width: int = BORDER_W,
                 color: tuple[int, int, int] = BLACK) -> None:
        super().__init__(sizes, pos, color)
        self.line_width: int = line_width

    def draw(self, wnd: pg.Surface) -> None:
        pg.draw.rect(wnd, self.color, self.rect, self.line_width)
