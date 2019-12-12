import random
import tkinter as tk

root = tk.Tk()
root.geometry('800x600')
root.title("Parz")
canvas_width = 600
canvas_height = 400

main_canvas = tk.Canvas(height=canvas_height, width=canvas_width, bg="#00f7ff")


def line_coordinates():
    x1 = float(input("X1 coordinate:"))
    y1 = float(input("Y1 coordinate:"))
    x2 = float(input("X2 coordinate:"))
    y2 = float(input("Y2 coordinate:"))
    main_canvas.create_line(x1, y1, x2, y2)


def framing(event):
    coordinates = event.x, event.y
    frame = tk.Frame(root, width=100, height=100)
    frame.bind("<Button-1>", coordinates)
    frame.pack()


line_coordinates()
main_canvas.pack()

root.mainloop()
