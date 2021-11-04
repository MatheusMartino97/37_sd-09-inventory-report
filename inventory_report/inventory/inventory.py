from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import xml.etree.ElementTree as ET
import csv
import json
# Primeira função inspirada no seguinte PR:
# https://github.com/tryber/sd-09-inventory-report/pull/10/files
def convert_xml_file_to_list(xml_file):
    converted_file = ET.parse(xml_file)
    root = converted_file.getroot()
    file_content = []
    for each_content in root:
        new_content = {}
        for each_element in each_content:
            new_content[each_element.tag] = each_element.text
        file_content.append(new_content)
    return file_content
class Inventory():
    @classmethod
    def import_data(cls, path, type):
        stock = []
        with open(path) as file:
            if path.endswith(".csv"):
                stock = list(csv.DictReader(file))
            if path.endswith(".json"):
                stock = list(json.load(file))
            if path.endswith(".xml"):
                stock = convert_xml_file_to_list(file)
        if type == "simples":
            return SimpleReport.generate(stock)
        else:
            return CompleteReport.generate(stock)