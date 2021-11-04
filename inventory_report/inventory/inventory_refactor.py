from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.inventory_iterator import InventoryIterator
from collections.abc import Iterable
import xml.etree.ElementTree as ET


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


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, path, type):
        self.data.extend(self.importer.import_data(path))
        if type == "simples":
            return SimpleReport.generate(self.data)
        if type == "completo":
            return CompleteReport.generate(self.data)