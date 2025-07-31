import myfunctions as mf
import turtle as t

t.shape("turtle")

t.onkeypress(mf.go_right, "Right")
t.onkeypress(mf.go_left, "Left")
t.onkeypress(mf.go_up, "Up")
t.onkeypress(mf.go_down, "Down")

t.onkeypress(mf.background_color, "b")
t.onkeypress(mf.change_color, "c")
t.onkeypress(mf.pen_size_up, "p")
t.onkeypress(mf.pen_size_down, "m")

t.onkeypress(mf.pen_updown, "space")
t.onkeypress(mf.clear, "Escape")

t.onkeypress(mf.polygon1, "1")
t.onkeypress(mf.polygon2, "2")
t.onkeypress(mf.polygon3, "3")
t.onkeypress(mf.polygon4, "4")
t.onkeypress(mf.polygon5, "5")
t.onkeypress(mf.polygon6, "6")
t.onkeypress(mf.polygon7, "7")
t.onkeypress(mf.polygon8, "8")
t.onkeypress(mf.polygon9, "9")


t.listen()
t.mainloop()