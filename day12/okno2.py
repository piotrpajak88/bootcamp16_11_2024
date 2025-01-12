import tkinter as tk

num = 1

def on_click():
    global num
    print(f"Przycisk zostal nacisniety po raz {num}")
    num += 1

app = tk.Tk()
app.title("Przyklad")

# do okienka dodajemy button
button =  tk.Button(app, text = "Kliknij mnie", command = on_click) # podajemy referencje do funkcji

button.pack()

app.mainloop()
