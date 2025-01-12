import tkinter as tk

def show_text():
    text = entry.get()
    print(f"Wprowadzony text: {text}")

app = tk.Tk()
app.title("Pole wprowadzania")

entry = tk.Entry(app)
entry.pack()

button = tk.Button(app, text = "Pokaz tekst", command = show_text)
button.pack()

app.mainloop()
