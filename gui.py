import tkinter as t

import termkillship as s

root= t.Tk()
root.geometry("480x780")
tui = s.tui

bg = t.PhotoImage(file="b.png")
p0 = t.PhotoImage(file="0.png")
p1 = t.PhotoImage(file="1.png")
p2 = t.PhotoImage(file="2.png")
p3 = t.PhotoImage(file="3.png")
p4 = t.PhotoImage(file="4.png")


canvas1 = t.Canvas( root, width = 480,height = 780)
root.resizable(0,0)
canvas1.pack(fill = "both", expand = False)
canvas1.create_image( 0, 0, image = bg, anchor = "nw")




tt = False
te = 0

def dir_d():
  global tui  # noqa: PLW0602
  s.move(tui,"d")

def dir_a():
  global tui  # noqa: PLW0602
  s.move(tui,"a")

dira = t.Button(text="«<",width=225,height=40,command=dir_a)
dird = t.Button(text=">»",width=225,height=40,command=dir_d)


canvas1.create_window(120,757,width=225,height=40,window=dira)
canvas1.create_window(360,757,width=225,height=40,window=dird)


def _loop():
  global tui, p0,p1,p2,p3,p4,te,tt  # noqa: PLW0602
  te += 1  
  canvas1.delete("fg")
  if te == 31 :
    tt = True
    te = 0
  s.fire(tui,tt)
  tt = False
  #root.bind('<KP_Left>',dir_a)
  #root.bind('<KeyPress_Right>',dir_d)
  #root.bind('<Return>',lambda:"p" in print("io"))
  s.gedraw(canvas1,tui,p0,p1,p2,p3,p4)
  
  
  
  root.after(25,_loop)




root.after(100,_loop)
root.mainloop()
