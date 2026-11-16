# Iteration of Black and White

A terminal puzzle game inspired by *Lights Out*. Players transform a binary board into a target pattern by toggling cells, racing against a time limit while trying to match the shortest known solution.

## Game rule

Selecting a cell flips the selected cell and its neighbors above, below, left, and right. The objective is to make the left board match the target shown on the right.

```text
Before       After selecting (2, 2)
101          101
000          001
101          110
```

## Features

- interactive terminal interface using Python `curses`;
- mouse and keyboard input;
- Easy (5×5), Medium (7×7), and Hard (9×9) boards;
- 15 missions per difficulty level;
- countdown timer and failure handling;
- reset and single-step undo;
- persistent top-three completion times;
- best-solution hints after repeated attempts;
- tutorial, scoreboard, and hidden completion content.

## Requirements

- Python 3
- a terminal with color, mouse, and `curses` support

On Linux and macOS, `curses` is normally included. On Windows, install `windows-curses`:

```bash
pip install windows-curses
```

## Run

```bash
git clone https://github.com/LittleLisa18/Iteration-of-Black-and-White.git
cd Iteration-of-Black-and-White
python3 main.py
```

Use a large terminal window so both boards and controls remain visible.

## Controls

| Input | Action |
| --- | --- |
| Arrow keys + Enter | Navigate menus |
| Mouse click | Select a menu item or board cell |
| Space | Enter a cell using row and column coordinates |
| `r` | Reset the current board |
| `w` | Undo the previous move |
| `b` | Request the best solution when available |
| `q` | Return to the previous screen |

## Difficulty and scoring

Each difficulty contains 15 missions. A mission is completed when the current board matches its target before time expires. Completion times are saved in `scoreboard.txt`, where the three fastest results for each mission are retained.

After five failed attempts, the best-solution view is unlocked. Completing a mission with the optimal sequence also unlocks a special reward screen.

## Repository structure

| Path | Description |
| --- | --- |
| `main.py` | Game logic, UI, input threads, timer, and menu flow |
| `Image/` | ASCII frames and terminal visual assets |
| `scoreboard.txt` | Persistent mission records |
| `scoreboard_init.py` | Scoreboard initialization helper |

## Troubleshooting

- If the layout is clipped, maximize the terminal or reduce its font size.
- If mouse input is unavailable, use keyboard coordinate-entry mode.
- Run from the repository root so relative asset paths resolve correctly.
