# A simple application of the xcanvas module
# Intended for applications with a single Canvas window
# The name of this Canvas is simply: canvas
# (but you can change it to any name you like)
# Once you load this module, you can use this canvas object to draw your figures ...

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
    id = canvas.create_rectangle(100, 120, 400, 230, width=2, outline="blue", fill="yellow")
    print("Rectangle 1 id:", id)
    canvas.create_text(200, 180, text="Rectangle 1", fill="maroon", font=("Consolas", 15, "bold"))

    id = canvas.create_rectangle(400, 320, 600, 530, width=5, outline="darkblue", fill="cyan")
    print("Rectangle 2 id:", id)
    canvas.create_text(500, 470, text="Rectangle 2", fill="Darkblue", font=("Times New Roman", 18, "bold"))

    id = canvas.create_line(200, 50, 500, 430, width=3, fill="DarkOrange")
    print("Line 1 id:", id)

    id = canvas.create_line(200, 60, 500, 440, width=3, fill="DarkOrange", dash=(2,3))
    print("Line 2 id:", id)

    print("Canvas Scroll Region:", canvas["scrollregion"])

    id = canvas.create_oval(100, 420, 300, 620, width=3, outline="darkgreen", fill="cornsilk")
    print("Circle id:", id)
    canvas.create_text(200, 520, text="Circle", fill="maroon", font=("Consolas", 15, "bold"))

    id = canvas.create_oval(450, 120, 650, 240, width=5, outline="goldenrod4", fill="tan")
    print("Ellipse id:", id)
    canvas.create_text(550, 180, text="Ellipse", fill="white", font=("Copperplate Gothic Bold", 21, "bold"))

    show_canvas()


def test2():
    # Hide the main canvas
    canvas.hide()
    # We can actually create multiple canvas instances !
    rootwin1 = tk.Tk()
    canvas1 = XCanvas(rootwin1, width=1000, height=800, bg="white")
    canvas1.create_rectangle(100, 120, 400, 230, width=2, outline="blue", fill="yellow")
    canvas1.create_rectangle(400, 320, 600, 530, width=2, outline="red", fill="cyan")
    canvas1.create_line(200, 50, 500, 430, width=3, fill="blue")

    rootwin2 = tk.Tk()
    canvas2 = XCanvas(rootwin2, width=1000, height=800, bg="gray90")
    canvas2.create_rectangle(100, 120, 400, 230, width=2, outline="blue", fill="orange")
    canvas2.create_rectangle(400, 320, 600, 530, width=2, outline="red", fill="yellow")
    canvas2.create_line(200, 50, 500, 430, width=3, fill="red")

    show_canvas()

if __name__ == "__main__":
    test1()
    #test2()


