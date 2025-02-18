import tkinter as tk

class ToggleSwitch(tk.Canvas):
    def __init__(self, master, variable=None, width=50, height=24,
                 on_color="#4CAF50", off_color="#BDBDBD", slider_color="white", **kwargs):
        super().__init__(master, width=width, height=height, highlightthickness=0, bd=0, bg="black", **kwargs)
        self.width = width
        self.height = height
        self.on_color = on_color
        self.off_color = off_color
        self.slider_color = slider_color
        self.radius = height / 2
        self.variable = variable if variable is not None else tk.BooleanVar(value=False)
        self.bind("<Button-1>", self.toggle)
        self.draw_switch()

    def draw_switch(self):
        self.delete("all")
        current = self.variable.get()
        track_color = self.on_color if current else self.off_color
        r = self.radius
        w = self.width
        h = self.height

        # Draw track
        self.create_oval(0, 0, 2*r, h, fill=track_color, outline=track_color)
        self.create_oval(w-2*r, 0, w, h, fill=track_color, outline=track_color)
        self.create_rectangle(r, 0, w-r, h, fill=track_color, outline=track_color)

        # Draw slider
        slider_d = h - 4
        slider_x = (w - h + 2) if current else 2
        self.create_oval(slider_x, 2, slider_x + slider_d, 2 + slider_d,
                         fill=self.slider_color, outline=self.slider_color)

    def toggle(self, event=None):
        self.variable.set(not self.variable.get())
        self.draw_switch()
