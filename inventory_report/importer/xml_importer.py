from inventory_report.inventory.inventory import convert_xml_file_to_list
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    def import_data(path):
        with open(path) as xml_file:
            if path.endswith(".xml"):
                return convert_xml_file_to_list(xml_file)
            raise ValueError("Arquivo inválido")