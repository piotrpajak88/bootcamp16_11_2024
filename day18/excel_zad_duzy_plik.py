import openpyxl
#write_only = True efektywniej zarzadza zuzyciem pamieci
import lxml #przyspiesza proces zapisu

book = openpyxl.Workbook(write_only=True)
sheet = book.create_sheet()

for row in range(1000):
    sheet.append(list(range(200)))

book.save("openpyxl_optimized.xlsx")