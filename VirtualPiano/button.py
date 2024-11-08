import pygame as pg
from borders import RectangleBorder
from shapes import RectangleShape
from colors import WHITE, BLACK
from config import BORDER_W
from enumerations import ButtonState, MousePressed


class Button:
    def __init__(self,
                 pos: tuple[int, int],
                 size: tuple[int, int],
                 color: tuple[int, int, int] = WHITE,
                 border_color: tuple[int, int, int] = BLACK,
                 border_width: int = BORDER_W) -> None:
        self.rect: RectangleShape = RectangleShape(size, pos, color)
        self.border: RectangleBorder = RectangleBorder(size, pos, border_width, border_color)
        self.state: int = ButtonState.INACTIVE
        self.pressed: int = MousePressed.RELEASED
    
    def draw(self, wnd: pg.Surface) -> None:
        self.rect.draw(wnd)
        self.border.draw(wnd)
    
    def update(self) -> None:
        mouse_pos: tuple[int, int] = pg.mouse.get_pos()
        self.change_state(mouse_pos)
    
    def change_state(self, mouse_pos: tuple[int, int]) -> None:
        self.state = ButtonState.INACTIVE
        if self.rect.rect.collidepoint(mouse_pos[0], mouse_pos[1]):
            self.state = ButtonState.ON_HOVER
        if self.state == ButtonState.ON_HOVER:
            self.change_pressed()
    
    def change_pressed(self) -> None:
        mouse_pressed: tuple[bool, ...] = pg.mouse.get_pressed()
        self.pressed = MousePressed.RELEASED
        if mouse_pressed[0]:
            self.pressed = MousePressed.LEFT
        if mouse_pressed[2]:
            self.pressed = MousePressed.RIGHT
        if self.pressed != MousePressed.RELEASED:
            self.state = ButtonState.ACTIVE
