# Constants
SIZE: int = 64
ROWS: int = 5
COLS: int = 7
FPS: int = 30
FNT_SIZE: int = int(SIZE * .5)
BORDER_W: int = 2
VOLUME: float = 1

# Window settings
WND_WIDTH: int = SIZE * COLS
WND_HEIGHT: int = SIZE * ROWS
WND_SIZE: tuple[int, int] = WND_WIDTH, WND_HEIGHT
TITLE: str = 'VirtualPiano'

# Assets
ICON: str = 'Assets/Turtle.png'
FONT: str = 'Assets/SUSE-BOLD.ttf'
COM_NOTES: str = 'Assets/NotesPiano/'
notes: tuple[str, ...] = 'do', 're', 'mi', 'fa', 'sol', 'lja', 'si'
NOTES: tuple[str, ...] = tuple([f'{COM_NOTES}{note}.ogg' for note in notes])
