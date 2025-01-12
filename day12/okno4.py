import tkinter as tk

def on_value_changed(value):
    print(f"Zmieniono wartość suwaka: {value}")

app = tk.Tk()
app.title("Przyklad suwaka")

slider = tk.Scale(app, from_=0, to = 100, orient = tk.HORIZONTAL, command = on_value_changed)
slider.pack(side = tk.BOTTOM)

app.mainloop()