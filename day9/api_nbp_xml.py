from typing import List

import requests
import xml.etree.ElementTree as ET
from pydantic import BaseModel

url = "https://api.nbp.pl/api/exchangerates/tables/A/?format=xml"

response = requests.get(url)
print(response)
print(response.text)

xml_data = response.content

root = ET.fromstring(xml_data)
print(root)

table_name = root.find(".//Table").text
print(f"Table: {table_name}")

date = root.find(".//EffectiveDate").text
print(f"Data tabeli: {date}")

no = root.find(".//No").text
print(f"Numer tabeli: {no}")

rates = root.findall(".//Rate")
print(rates)

for rate in rates:
    currency = rate.find("Currency").text
    code = rate.find("Code").text
    mid = rate.find("Mid").text
    print(f"Waluta: {currency}, Kod: {code}, Cena średnia: {mid}")


# Waluta: bat (Tajlandia), Kod: THB, Cena średnia: 0.1205
# Waluta: dolar amerykański, Kod: USD, Cena średnia: 4.1512
# Waluta: dolar australijski, Kod: AUD, Cena średnia: 2.5794
# Waluta: dolar Hongkongu, Kod: HKD, Cena średnia: 0.5337
# Waluta: dolar kanadyjski, Kod: CAD, Cena średnia: 2.8849
# Waluta: dolar nowozelandzki, Kod: NZD, Cena średnia: 2.3252
# Waluta: dolar singapurski, Kod: SGD, Cena średnia: 3.0299
# Waluta: euro, Kod: EUR, Cena średnia: 4.2718
# Waluta: forint (Węgry), Kod: HUF, Cena średnia: 0.010299
# Waluta: frank szwajcarski, Kod: CHF, Cena średnia: 4.5658
# Waluta: funt szterling, Kod: GBP, Cena średnia: 5.1498
# Waluta: hrywna (Ukraina), Kod: UAH, Cena średnia: 0.0986
# Waluta: jen (Japonia), Kod: JPY, Cena średnia: 0.026398
# Waluta: korona czeska, Kod: CZK, Cena średnia: 0.1697
# Waluta: korona duńska, Kod: DKK, Cena średnia: 0.5727
# Waluta: korona islandzka, Kod: ISK, Cena średnia: 0.029769
# Waluta: korona norweska, Kod: NOK, Cena średnia: 0.3644
# Waluta: korona szwedzka, Kod: SEK, Cena średnia: 0.3726
# Waluta: lej rumuński, Kod: RON, Cena średnia: 0.8588
# Waluta: lew (Bułgaria), Kod: BGN, Cena średnia: 2.1841
# Waluta: lira turecka, Kod: TRY, Cena średnia: 0.1173
# Waluta: nowy izraelski szekel, Kod: ILS, Cena średnia: 1.1365
# Waluta: peso chilijskie, Kod: CLP, Cena średnia: 0.004129
# Waluta: peso filipińskie, Kod: PHP, Cena średnia: 0.0714
# Waluta: peso meksykańskie, Kod: MXN, Cena średnia: 0.2023
# Waluta: rand (Republika Południowej Afryki), Kod: ZAR, Cena średnia: 0.2210
# Waluta: real (Brazylia), Kod: BRL, Cena średnia: 0.6747
# Waluta: ringgit (Malezja), Kod: MYR, Cena średnia: 0.9225
# Waluta: rupia indonezyjska, Kod: IDR, Cena średnia: 0.00025641
# Waluta: rupia indyjska, Kod: INR, Cena średnia: 0.048407
# Waluta: won południowokoreański, Kod: KRW, Cena średnia: 0.002823
# Waluta: yuan renminbi (Chiny), Kod: CNY, Cena średnia: 0.5672
# Waluta: SDR (MFW), Kod: XDR, Cena średnia: 5.3801

class CurrencyRate(BaseModel):
    currency: str
    code: str
    mid: float


class ExchangeRateTable(BaseModel):
    table: str
    date: str
    number: str
    rates: List[CurrencyRate]

# deserializacja z uzyciem Pydantic
currency_rates = []
for rate in rates:
    currency = rate.find("Currency").text
    code = rate.find("Code").text
    mid = rate.find("Mid").text
    currency_rates.append(CurrencyRate(currency=currency, code=code, mid=float(mid)))

exchange_rates_table = ExchangeRateTable(
    table=table_name,
    date=date,
    number=no,
    rates=currency_rates
)

print(exchange_rates_table)