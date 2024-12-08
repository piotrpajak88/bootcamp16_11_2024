import main
import pakiet
from pakiet import fun
import pakiet.fun as pk

main.print_hi("Radek") # Hi, Radek

# pakiet.powitanie() #AttributeError: module 'pakiet' has no attribute 'powitanie'

# from pakiet import fun
fun.powitanie() # Cześć
fun.info() # Jestem pakietem

pk.powitanie()
pk.info()
# Cześć
# Jestem pakietem

# sterowanie widocznoscia elementow pakietu => sprawdz __init__.py
# __all__ = ['info']
pakiet.info()
# Jestem pakietem