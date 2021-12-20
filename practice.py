import tkinter as tk
def draw(canvas):
    pass
def makecanvas(w,h):
    root=tk.Tk()
    canvas=tk.Canvas(root,width=w,height=h)
    canvas.configure(bd=1)
    canvas.create_oval(10, 50, 110, 100)
    # canvas.create_rectangle(30,10,120, 80)
    canvas.pack()
    draw(canvas)
    root.mainloop()
print(makecanvas(100,100))