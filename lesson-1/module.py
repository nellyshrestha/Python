from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.screen import Screen
import sys

import pyjokes

joke=pyjokes.get_joke()
print(joke)


# def demo(screen):
#     effects = [
#         Cycle(
#             screen,
#             FigletText("NELLY", font='big'),
#             int(screen.height / 2 - 8)),
#         Cycle(
#             screen,
#             FigletText("Is", font='big'),
#             int(screen.height / 2 + 3)),
#         Cycle(
#             screen,
#             FigletText("Good", font='big'),
#             int(screen.height / 2 + 4)),
#         Stars(screen, 800)
#     ]
#     screen.play([Scene(effects, 500)])

# Screen.wrapper(demo)

def demo(screen):
    effects = [
        Cycle(
            screen,
            FigletText("NELLY", font='big'),
            int(screen.height / 2 - 6)),
        Cycle(
            screen,
            FigletText("Is", font='small'),
            int(screen.height / 2)),
        Cycle(
            screen,
            FigletText("Good", font='big'),
            int(screen.height / 2 + 6)),
        Stars(screen, 100)  # You can change the number of stars
    ]

    screen.play([Scene(effects, -1)], stop_on_resize=True)

# Run the screen wrapper safely
if __name__ == "__main__":
    try:
        Screen.wrapper(demo)
    except KeyboardInterrupt:
        sys.exit(0)