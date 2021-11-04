from datetime import datetime


def get_oldest_manufacturing_date(stock):
    oldest_manufacturing_date = min(
        each_product["data_de_fabricacao"] for each_product in stock
    )
    return oldest_manufacturing_date


def get_closest_expiration_date(stock):
    current_date = datetime.now().strftime('%Y-%m-%d')
    closest_expiration_date = [
        each_product["data_de_validade"]
        for each_product in stock
        if each_product["data_de_validade"] >= current_date
    ]
    closest_expiration_date.sort()
    return closest_expiration_date[0]


def get_greatest_company_stock(stock):
    greatest_company_stock = max(
        each_company["nome_da_empresa"] for each_company in stock
    )
    return greatest_company_stock


class SimpleReport:
    @classmethod
    def generate(cls, stock):
        oldest_manufacturing_date = get_oldest_manufacturing_date(stock)
        closest_expiration_date = get_closest_expiration_date(stock)
        greatest_company_stock = get_greatest_company_stock(stock)

        return (
            f"Data de fabricação mais antiga: {oldest_manufacturing_date}\n"
            f"Data de validade mais próxima: {closest_expiration_date}\n"
            f"Empresa com maior quantidade"
            f" de produtos estocados: {greatest_company_stock}\n"
        )
