import pygame as pg
from config import SIZE, WND_SIZE, TITLE, VOLUME, ICON, FPS, NOTES
from enumerations import MousePressed
from colors import WHITE, RED
from button import Button


pg.init()
WND: pg.Surface = pg.display.set_mode(WND_SIZE, pg.HWSURFACE)
icon: pg.Surface = pg.image.load(ICON).convert_alpha()
pg.display.set_caption(TITLE)
pg.display.set_icon(icon)


class VirtualPiano:
    def __init__(self) -> None:
        self.running: bool = True
        self.clock: pg.time.Clock = pg.time.Clock()
        self.sounds: list[pg.mixer.Sound] = [pg.mixer.Sound(path) for path in NOTES]
        [sound.set_volume(VOLUME) for sound in self.sounds]
        x_s: list[int] = [SIZE * i for i in range(len(self.sounds))]
        not_size: tuple[int, int] = SIZE, SIZE * 4
        self.notes: list[Button] = [Button((x, 0), not_size) for x in x_s]
        qt_pos: tuple[int, int] = 0, not_size[1]
        qt_size: tuple[int, int] = WND_SIZE[0], WND_SIZE[1] - not_size[1]
        self.button_quit: Button = Button(qt_pos, qt_size, color=RED, border_color=RED)
    
    def main(self) -> None:
        while self.running:
            WND.fill(WHITE)
            [note.draw(WND) for note in self.notes]
            [note.update() for note in self.notes]
            self.button_quit.draw(WND)
            self.button_quit.update()
            self.play_note()
            pg.display.flip()
            self.quit()
            self.event_loop()
            self.clock.tick(FPS)
    
    def quit(self) -> None:
        if self.button_quit.pressed == MousePressed.LEFT:
            self.running = False
    
    def play_note(self) -> None:
        for ind, note in enumerate(self.notes):
            if note.pressed == MousePressed.LEFT:
                self.sounds[ind].play()
            
    def event_loop(self) -> None:
        if not self.running:
            pg.quit()
            return
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
                pg.quit()

if __name__ == '__main__':
    app: VirtualPiano = VirtualPiano()
    app.main()
    