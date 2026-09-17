# Use lists of characters so we can modify individual positions

tui = [
    list("333333333"),
    list("000000000"),
    list("000000000"),
    list("000000000"),
    list("000000000"),
    list("000000000"),
    list("000000000"),
    list("000000000"),
    list("000000000"),
    list("000000000"),
    list("000000000"),
    list("000000000"),
    list("000020000")]


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

def move(tui,cmd=""):
    _x,_y= loca(tui,"2")
    if  cmd =="a" and _x == 0  or cmd =="d" and _x == len(tui[_y])-1 :
        pass

    elif cmd == "a" :
        tui[_y][_x-1]="2"
        tui[_y][_x] = "0"
    elif cmd == "d" :
        tui[_y][_x+1]="2"
        tui[_y][_x] = "0"
    else:
        pass



def gedraw(canva,tui,p0,p1,p2,p3,p4) :
  y = 0
  for yy in tui :
    x = 0
    for xx in yy :
      imgs = {"0":p0, "1":p1 ,"2":p2,"3":p3 , "4":p4}
      canva.create_image( x,y,anchor="nw",image = imgs[xx] , tags = "fg")
      x += 54
    y += 54
