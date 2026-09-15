import tkinter as t
import termkillship as s

root= t.Tk()
root.geometry("480x768")
tui = s.tui

bg = t.PhotoImage(file="b.png")
p0 = t.PhotoImage(file="00.png")
p1 = t.PhotoImage(file="11.png")
p2 = t.PhotoImage(file="22.png")
p3 = t.PhotoImage(file="33.png")
p4 = t.PhotoImage(file="44.png")


def gedraw(canva,tui,p0,p1,p2,p3,p4) :
  y = 0
  for yy in tui :
    x = 0
    for xx in yy :
      imgs = {"0":p0, "1":p1 ,"2":p2,"3":p3 , "4":p4}
      canva.create_image(x,y,anchor="nw",image = imgs[xx] , tags = "fg")
      x += 48
    y += 48



canvas1 = t.Canvas( root, width = 480,height = 768)
root.resizable(0,0)
canvas1.pack(fill = "both", expand = False)
canvas1.create_image( 0, 0, image = bg, anchor = "nw")
tt = False
t = 0
def _loop():
  global tui ,p0 ,p1 ,p2 ,p3 ,p4 ,t,tt
  t += 1
  
  canvas1.delete("fg")
  canvas1.create_image( 0, 0, image = bg, anchor = "nw")
  if t % 7 == 0 :
    tt = True
  s.fire(tui,tt)
  tt = False
  gedraw(canvas1,tui,p0,p1,p2,p3,p4)
  root.after(400,_loop)
  
root.after(1000,_loop)


root.mainloop()
