from m5stack import *
from m5ui import *
from uiflow import *
from emoji import Emoji


def position_mark_all_clear():
  global hor, diag, diag2
  hor = [0] * 8
  diag = [0] * 16
  diag2 = [0] * 16

def position_is_free(row, col):
  global hor, diag, diag2
  return hor[col] != 1 and diag2[row + col] != 1 and diag[row - col + QUEENS-1] != 1

def position_mark_used(row, col):
  emoji0.draw_square(row, col, 0xff0000)
  position_mark_value(row, col, 1)

def position_mark_free(row, col):
  emoji0.draw_square(row, col, 0xffffff)
  position_mark_value(row, col, 0)

def position_mark_value(row, col, value):
  global hor, diag, diag2
  # Mark the horizontal and diagonals positions
  hor[col] = value
  diag[row - col + QUEENS -1] = value
  diag2[row + col] = value

# Place a queen on the board, obying the rules
def place_a_queen(row):
  global solvcount, QUEENS
  
  if row < QUEENS:
    for i in range(QUEENS):
      if position_is_free(row, i):
        position_mark_used(row, i)
        # Try the next row
        place_a_queen(row + 1)
        position_mark_free(row, i)
  else:
    solvcount = solvcount + 1
    solved.setText(str(solvcount))
    speaker.tone(1800, 50)
    wait(1)

# Init screen
setScreenColor(0x222222)
solved = M5TextBox(5, 6, "0", lcd.FONT_DejaVu40,0xddf606, rotate=0)

hor = None
diag = None
solvcount = 0
diag2 = None
QUEENS = 8

# Place 8 queens on the chess board, show all solutions
# See: https://en.wikipedia.org/wiki/Eight_queens_puzzle
emoji0 = Emoji(QUEENS,QUEENS, 15, 9)
position_mark_all_clear()
solvcount = 0
place_a_queen(0)
