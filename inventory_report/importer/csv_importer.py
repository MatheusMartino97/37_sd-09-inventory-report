import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    def import_data(path):
        with open(path) as csv_file:
            if path.endswith(".csv"):
                return list(csv.DictReader(csv_file))
            raise ValueError("Arquivo inválido")
