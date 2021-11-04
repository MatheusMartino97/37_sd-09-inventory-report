import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    def import_data(path):
        with open(path) as json_file:
            if path.endswith(".json"):
                return list(json.load(json_file))
            raise ValueError("Arquivo inválido")