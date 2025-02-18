import tkinter as tk

class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tipwindow = None
        widget.bind("<Enter>", self.show_tip)
        widget.bind("<Leave>", self.hide_tip)

    def show_tip(self, event=None):
        if self.tipwindow or not self.text:
            return
        x = self.widget.winfo_rootx() + 20
        y = self.widget.winfo_rooty() + 20
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.configure(bg="white")
        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                         background="white", foreground="#212121",
                         relief=tk.SOLID, borderwidth=1,
                         font=("Segoe UI", 8, "bold"), wraplength=200)
        label.pack(ipadx=1)
        tw.update_idletasks()
        tip_width = tw.winfo_width()
        tip_height = tw.winfo_height()
        screen_width = self.widget.winfo_screenwidth()
        screen_height = self.widget.winfo_screenheight()
        if x + tip_width > screen_width:
            x = screen_width - tip_width - 10
        if y + tip_height > screen_height:
            y = screen_height - tip_height - 10
        tw.wm_geometry("+%d+%d" % (x, y))

    def hide_tip(self, event=None):
        if self.tipwindow:
            self.tipwindow.destroy()
            self.tipwindow = None