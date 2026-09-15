# Use lists of characters so we can modify individual positions

tui = [list("333333333"), list("000000000"), list("000000000"), list("000000000"), list("000000000"), list("000000000"), list("000000000"),list("000000000"),list("000000000"),list("000000000"),list("000000000"),list("000000000"), list("000020000")]

def redraw(tui):
    for row in tui:
        print(''.join(row))   # join list into a string

def loca(tui, st):
    """Return (x, y) of first occurrence of st, or None if not found."""
    for y, row in enumerate(tui):
        for x, ch in enumerate(row):
            if ch == st:
                return x, y
    return None

def fire(tui,yes=True):
    pos1 = loca(tui, "1")
    if pos1 is not None:
        x, y = pos1
        yw = y - 1          # row above current
        if y == 0:
            # At the top: just remove the "1"
            tui[y][x] = "0"
        else:
            if tui[yw][x] == "0":
                # Move upward
                tui[yw][x] = "1"
                tui[y][x] = "0"
            else:
                # Hit something: remove both the "1" and the obstacle
                tui[yw][x] = "0"
                tui[y][x] = "0"
    elif yes == True:
        # No "1" exists: create one just above "2"
        pos2 = loca(tui, "2")
        if pos2 is not None:
            x, y = pos2
            y1 = y - 1
            if y1 >= 0:          # avoid going out of bounds
                tui[y1][x] = "1"
#def anti_fire(tui) :
#  for y in 

