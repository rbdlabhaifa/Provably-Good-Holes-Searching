import gc
import random

from matplotlib.figure import Figure
from matplotlib.widgets import RectangleSelector
import easygui
import PIL
import cv2
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

import tkinter as tk
from PIL import ImageTk, Image

coordinates = {}
image_ = None

# def func():
#
#
#     class MousePositionTracker(tk.Frame):
#         """ Tkinter Canvas mouse position widget. """
#
#         def __init__(self, canvas):
#             self.canvas = canvas
#             self.canv_width = self.canvas.cget('width')
#             self.canv_height = self.canvas.cget('height')
#             self.reset()
#
#             # Create canvas cross-hair lines.
#             xhair_opts = dict(dash=(3, 2), fill='white', state=tk.HIDDEN)
#             self.lines = (self.canvas.create_line(0, 0, 0, self.canv_height, **xhair_opts),
#                           self.canvas.create_line(0, 0, self.canv_width, 0, **xhair_opts))
#
#         def cur_selection(self):
#             return (self.start, self.end)
#
#         def begin(self, event):
#             self.hide()
#             self.start = (event.x, event.y)  # Remember position (no drawing).
#
#         def update(self, event):
#             self.end = (event.x, event.y)
#
#             self._update(event)
#             self._command(self.start, (event.x, event.y))  # User callback.
#
#         def _update(self, event):
#             # Update cross-hair lines.
#             self.canvas.coords(self.lines[0], event.x, 0, event.x, self.canv_height)
#             self.canvas.coords(self.lines[1], 0, event.y, self.canv_width, event.y)
#
#             self.show()
#
#         def reset(self):
#             self.start = self.end = None
#
#         def hide(self):
#             self.canvas.itemconfigure(self.lines[0], state=tk.HIDDEN)
#             self.canvas.itemconfigure(self.lines[1], state=tk.HIDDEN)
#
#         def show(self):
#             self.canvas.itemconfigure(self.lines[0], state=tk.NORMAL)
#             self.canvas.itemconfigure(self.lines[1], state=tk.NORMAL)
#
#         def autodraw(self, command=lambda *args: None):
#             """Setup automatic drawing; supports command option"""
#             self.reset()
#             self._command = command
#             self.canvas.bind("<Button-1>", self.begin)
#             self.canvas.bind("<B1-Motion>", self.update)
#             self.canvas.bind("<ButtonRelease-1>", self.quit)
#
#         def quit(self, event):
#             self.hide()  # Hide cross-hairs.
#             self.calHoles()
#             self.reset()
#
#         def calHoles(self):
#             counter = 0
#             print(self.start, self.end)
#             print("coordinates = ", coordinates)
#             for label in coordinates:
#                 if coordinates[label][0] >= min(self.start[0], self.end[0]) and coordinates[label][0] <= max(
#                         self.start[0], self.end[0]) and coordinates[label][1] >= min(self.start[1], self.end[1]) and \
#                         coordinates[label][1] <= max(self.start[1], self.end[1]):
#                     counter += 1
#             easygui.msgbox(str(counter) + " holes")
#             print(counter)
#
#     class SelectionObject:
#         """ Widget to display a rectangular area on given canvas defined by two points
#             representing its diagonal.
#         """
#
#         def __init__(self, canvas, select_opts):
#             # Create attributes needed to display selection.
#             self.canvas = canvas
#             self.select_opts1 = select_opts
#             self.width = self.canvas.cget('width')
#             self.height = self.canvas.cget('height')
#
#             # Options for areas outside rectanglar selection.
#             select_opts1 = self.select_opts1.copy()  # Avoid modifying passed argument.
#             select_opts1.update(state=tk.HIDDEN)  # Hide initially.
#             # Separate options for area inside rectanglar selection.
#             select_opts2 = dict(dash=(2, 2), fill='', outline='white', state=tk.HIDDEN)
#
#             # Initial extrema of inner and outer rectangles.
#             imin_x, imin_y, imax_x, imax_y = 0, 0, 1, 1
#             omin_x, omin_y, omax_x, omax_y = 0, 0, self.width, self.height
#
#             self.rects = (
#                 # Area *outside* selection (inner) rectangle.
#                 self.canvas.create_rectangle(omin_x, omin_y, omax_x, imin_y, **select_opts1),
#                 self.canvas.create_rectangle(omin_x, imin_y, imin_x, imax_y, **select_opts1),
#                 self.canvas.create_rectangle(imax_x, imin_y, omax_x, imax_y, **select_opts1),
#                 self.canvas.create_rectangle(omin_x, imax_y, omax_x, omax_y, **select_opts1),
#                 # Inner rectangle.
#                 self.canvas.create_rectangle(imin_x, imin_y, imax_x, imax_y, **select_opts2)
#             )
#
#         def update(self, start, end):
#             # Current extrema of inner and outer rectangles.
#             imin_x, imin_y, imax_x, imax_y = self._get_coords(start, end)
#             omin_x, omin_y, omax_x, omax_y = 0, 0, self.width, self.height
#
#             # Update coords of all rectangles based on these extrema.
#             self.canvas.coords(self.rects[0], omin_x, omin_y, omax_x, imin_y),
#             self.canvas.coords(self.rects[1], omin_x, imin_y, imin_x, imax_y),
#             self.canvas.coords(self.rects[2], imax_x, imin_y, omax_x, imax_y),
#             self.canvas.coords(self.rects[3], omin_x, imax_y, omax_x, omax_y),
#             self.canvas.coords(self.rects[4], imin_x, imin_y, imax_x, imax_y),
#
#             for rect in self.rects:  # Make sure all are now visible.
#                 self.canvas.itemconfigure(rect, state=tk.NORMAL)
#
#         def _get_coords(self, start, end):
#             """ Determine coords of a polygon defined by the start and
#                 end points one of the diagonals of a rectangular area.
#             """
#             return (min((start[0], end[0])), min((start[1], end[1])),
#                     max((start[0], end[0])), max((start[1], end[1])))
#
#         def hide(self):
#             for rect in self.rects:
#                 self.canvas.itemconfigure(rect, state=tk.HIDDEN)
#
#     class Application(tk.Frame):
#         # Default selection object options.
#         SELECT_OPTS = dict(dash=(2, 2), stipple='gray25', fill='red',
#                            outline='')
#
#         def __init__(self, parent, *args, **kwargs):
#             super().__init__(parent, *args, **kwargs)
#
#             path = "images\current.tif"
#             image_ = ImageTk.PhotoImage(Image.open(path))
#             self.canvas = tk.Canvas(root, width=image_.width(), height=image_.height(),
#                                     borderwidth=0, highlightthickness=0)
#
#             self.canvas.pack(expand=True)
#
#             self.canvas.create_image(0, 0, image=image_, anchor=tk.NW)
#             self.canvas.img = image_  # Keep reference.
#
#             # Create selection object to show current selection boundaries.
#             self.selection_obj = SelectionObject(self.canvas, self.SELECT_OPTS)
#
#             # Callback function to update it given two points of its diagonal.
#             def on_drag(start, end, **kwarg):  # Must accept these arguments.
#                 self.selection_obj.update(start, end)
#
#             # Create mouse position tracker that uses the function.
#             self.posn_tracker = MousePositionTracker(self.canvas)
#
#             self.posn_tracker.autodraw(command=on_drag)  # Enable callbacks.
#
#
#     WIDTH, HEIGHT = 900, 900
#     BACKGROUND = 'grey'
#     TITLE = 'Image Cropper'
#
#     root = tk.Tk()
#     root.title(TITLE)
#     root.geometry('%sx%s' % (WIDTH, HEIGHT))
#     root.configure(background=BACKGROUND)
#
#     app = Application(root, background=BACKGROUND)
#     app.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE)
#
#     app.mainloop()

def line_select_callback(eclick, erelease):
    'eclick and erelease are the press and release events'
    x1, y1 = eclick.xdata, eclick.ydata
    x2, y2 = erelease.xdata, erelease.ydata
    counter = 0
    for label in coordinates:
        if coordinates[label][0] >= min(y1, y2) and coordinates[label][0] <= max(
                y1, y2) and coordinates[label][1] >= min(x1, x2) and \
                coordinates[label][1] <= max(x1, x2):
            counter += 1

    print("(%3.2f, %3.2f) --> (%3.2f, %3.2f)" % (x1, y1, x2, y2))
    print(" The button you used were: %s %s" % (eclick.button, erelease.button))

    if erelease.button:
        easygui.msgbox(str(counter) + " holes")



def toggle_selector(event):
    print(' Key pressed.')
    if event.key in ['Q', 'q'] and toggle_selector.RS.active:
        print(' RectangleSelector deactivated.')
        toggle_selector.RS.set_active(False)
    if event.key in ['A', 'a'] and not toggle_selector.RS.active:
        print(' RectangleSelector activated.')
        toggle_selector.RS.set_active(True)



def algorithm(originImg):

    img = np.copy(originImg)
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    hist = cv.calcHist([img], [0], None, [256], (0, 255))

    hist = [h[0] for h in hist][1:]
    for i in range(1, 255):
        hist[i] = hist[i] + hist[i - 1]
    img[img == 0] = 255
    imSize = img.shape[0] * img.shape[1]
    hist = [h / imSize for h in hist]
    bi = 0
    while hist[bi] <= 0.0009:
        bi += 1

    ret, th1 = cv.threshold(img, bi, 255, cv.THRESH_BINARY_INV)
    for k in range(2):
        coords = np.column_stack(np.where(th1 != 0))
        rows, cols = th1.shape
        th1_cpy = np.copy(th1)
        for (i, j) in coords:
            if 0 < i < rows - 1 and 0 < j < cols - 1:
                cnt = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if th1_cpy[i + x][j + y] != 0:
                            cnt += 1
                if cnt < 9:
                    th1[i][j] = 0
            else:
                th1[i][j] = 0

    ret, labels = cv.connectedComponents(th1)
    rows, cols = th1.shape

    del img
    gc.collect()
    img = np.copy(originImg)
    labels = np.array(labels)
    for label in range(1, ret):
        coords = np.where(labels == label)
        coord = np.mean(coords, axis=1, dtype=int)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        coordinates[label] = coord
        print(f'{label}={coord}')
        try:
            cv2.putText(originImg, str(label), (coord[1] - 5, coord[0] + 5), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 5)
        except:
            print("cant count circles")
        img = cv.circle(originImg, center=(coord[1], coord[0]), radius=50, color=color, thickness=20)


    fig, current_ax = plt.subplots()  # make a new plotting range

    plt.imshow(img)

    print("\n      click  -->  release")
    # drawtype is 'box' or 'line' or 'none'
    toggle_selector.RS = RectangleSelector(current_ax, line_select_callback,
                                           drawtype='box', useblit=True,
                                           button=[1, 3],  # don't use middle button
                                           minspanx=5, minspany=5,
                                           spancoords='pixels',
                                           interactive=True)
    plt.connect('key_press_event', toggle_selector)

    plt.show()

    return ret, img






