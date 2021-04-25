import turtle

t = turtle.Pen()
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']

for x in range(380):
    t.pencolor(colors[x % 6])
    t.forward(x)
    # Different image
    t.left(35)
    # Square
    t.left(90)
    # t.left(50) smoother spiral
    # t.left(70) spiral
    # t.left(70) with t.left(90) make a star

ts = turtle.getscreen()
ts.getcanvas().postscript(file="drawing.eps")
