from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


def get_company_products_qtty(stock):
    companies = [
        each_company["nome_da_empresa"]
        for each_company in stock
    ]
    report = ''
    products_qtty = Counter(companies)
    for company_name in products_qtty:
        report += f"- {company_name}: {products_qtty[company_name]}\n"
    return f"Produtos estocados por empresa: \n{report}"


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, stock):
        simple_report = SimpleReport.generate(stock)
        complete_report = get_company_products_qtty(stock)
        return f"{simple_report}\n{complete_report}"