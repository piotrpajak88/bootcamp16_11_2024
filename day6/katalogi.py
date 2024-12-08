import shutil
from pathlib import Path

base_path = Path('../ops_example')
base_path2 = Path('ops_example/D')

if base_path.exists() and base_path.is_dir():
    shutil.rmtree(base_path) #usuniecie calego drzewa katalogow

base_path.mkdir() #utworzenie nowego katalogu

path_b = base_path / 'A' / 'B'
path_c = base_path / 'A' / 'C'
path_d = base_path / 'A' / 'D'

# path_b.mkdir()
# FileNotFoundError: [WinError 3] System nie może odnaleźć określonej ścieżki: '..\\ops_example\\A\\B'

path_b.mkdir(parents=True) #utworzenie katalogu i wszystkich jego nadrzędnych katalogów\
path_c.mkdir() # bo katalog A juz istnieje

for filename in ('ex1.txt', 'ex2.txt', 'ex3.txt'):
    with open(path_b / filename, "w", encoding='utf-8') as stream:
        stream.write(f"Content of {filename}")

# przenosi pliki z katalogu B do katalogu D, usunie katalog B
shutil.move(path_b, path_d)
ex1 = path_d / 'ex1.txt'
#zmiana nazwy pliku
ex1.rename(ex1.parent / 'ex1_renamed.log')

print(base_path.absolute())
# C:\Users\88iro\PycharmProjects\bootcamp16_11_2024\pythonProject2\day6\..\ops_example
print(base_path.name)
# ops_example
print(base_path.parent.absolute())
# C:\Users\88iro\PycharmProjects\bootcamp16_11_2024\pythonProject2\day6\..

print(base_path.suffix)
print(ex1.suffix)
print(base_path.parts)
print(base_path2.parts)
#
# .txt
# ('..', 'ops_example')
# ('ops_example', 'D')

