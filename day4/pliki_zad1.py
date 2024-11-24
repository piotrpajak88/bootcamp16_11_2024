# praca z plikami

# t = open("nazwa pliku","parametr")

# context manager
# with
# to pozwala na bezpieczniejsza prace z plikami

# ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
with open("test.log","w",encoding='utf-8') as fh: # filehandler
    fh.write("Powitanie\n")
    fh.write("Kolejne\n")
    fh.write("Jeszcze jedno\n")

with open("../test.log","w") as fh: # filehandler, ten plik bedzie w nadrzednym katalogu
    fh.write("Powitanie\n")

with open("../test.log","w") as fh: # filehandler, ten plik bedzie w nadrzednym katalogu
    fh.write("Nadpisane\n")

# with open("../test.log","x") as fh: # filehandler, ten plik bedzie w nadrzednym katalogu
#     fh.write("Powitanie\n")
# FileExistsError: [Errno 17] File exists: '../test.log'

# with open("../test2.log","x") as fh: # filehandler, ten plik bedzie w nadrzednym katalogu
#     fh.write("Nadpisane\n")

with open("test.log","a",encoding='utf-8') as file:
    file.write("Dodane\n")
    file.write("Dodane\n")
    file.write("Dodane\n")
    file.write("Dośdane\n")

with open("test.log","r",encoding='utf-8') as f:
    lines = f.read()

# encoding='utf-8' - ustawienie kodowania na utf-8
# nalezy to przy kazdym open danego pliku wstawiac, bo mozna popsuc plik
# nalezy to dodać jak sa polskie znaki, bo inaczej źle zapisze do pliku

print(lines)
# Powitanie
# Kolejne
# Jeszcze jedno
# Dodane
# Dodane
# Dodane
# Dośdane

