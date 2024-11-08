import pygame as pg
from colors import WHITE


class RectangleShape:
    """Implements the Shape interface for rectangle"""
    def __init__(self,
                 sizes: tuple[int, int],
                 pos: tuple[int, int],
                 color: tuple[int, int, int] = WHITE) -> None:
        self.rect: pg.rect.Rect = pg.rect.Rect(pos[0], pos[1], sizes[0], sizes[1])
        self.color: tuple[int, int, int] = color

    def draw(self, wnd: pg.Surface) -> None:
        pg.draw.rect(wnd, self.color, self.rect)

    def resize(self, sizes: tuple[int, int]) -> None:
        if sizes != (self.rect.width, self.rect.height):
            self.rect.width, self.rect.height = sizes

    def change_color(self, color: tuple[int, int, int]) -> None:
        if color != self.color:
            self.color = color

    @property
    def pos(self) -> tuple[int, int]:
        return self.rect.left, self.rect.top

    @pos.setter
    def pos(self, pos: tuple[int, int]) -> None:
        self.rect.left, self.rect.top = pos

    @property
    def sizes(self) -> tuple[int, int]:
        return self.rect.width, self.rect.height
