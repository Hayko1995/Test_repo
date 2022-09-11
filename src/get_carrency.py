import requests
from xml.etree import ElementTree
import xmltodict

def get_carency():
    response = requests.get('https://www.cbr.ru/scripts/XML_daily.asp')

    dict_data = xmltodict.parse(response.content)
    for data in dict_data["ValCurs"]["Valute"]:
        if data["Name"]== "Доллар США":
            return data
