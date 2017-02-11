# A simple application of the xcanvas module

from xcanvas import *

try:
    rootWindow
except NameError:
    rootWindow = tk.Tk()

# This is where we create our canvas instance
# The name canvas referes to it when you import this module
canvas = XCanvas(rootWindow, width=1000, height=800, bg="white")

def show_canvas():
    tk.mainloop()

#-----------------------------------------------------------------------

def test1():
    id = canvas.create_rectangle(100, 120, 400, 230, width=2, outline='blue', fill='yellow')
    id = canvas.create_rectangle(400, 320, 600, 530, width=2, outline='blue', fill='yellow')
    id = canvas.create_line(200, 50, 500, 430, width=3, fill='blue')
    #print(canvas['scrollregion'])
    canvas.show()
    show_canvas()


def test2():
    # Hide the main canvas
    canvas.hide()
    # We can actually create multiple canvas instances !
    rootwin1 = tk.Tk()
    canvas1 = XCanvas(rootwin1, width=1000, height=800, bg="white")
    canvas1.create_rectangle(100, 120, 400, 230, width=2, outline='blue', fill='yellow')
    canvas1.create_rectangle(400, 320, 600, 530, width=2, outline='blue', fill='yellow')
    canvas1.create_line(200, 50, 500, 430, width=3, fill='blue')

    rootwin2 = tk.Tk()
    canvas2 = XCanvas(rootwin2, width=1000, height=800, bg="gray90")
    canvas2.create_rectangle(100, 120, 400, 230, width=2, outline='red', fill='yellow')
    canvas2.create_rectangle(400, 320, 600, 530, width=2, outline='red', fill='yellow')
    canvas2.create_line(200, 50, 500, 430, width=3, fill='red')

    show_canvas()

if __name__ == "__main__":
    #test1()
    test2()


