# Sukurti programa, kuri ja paleidus priimtu du parametrus islaidas ir iplaukas eurais. 
# Ta programa turi paskaiciuoti:
# Visu isplauku ir iplauku menesinius vidurkius
# Turi paskaiciuoti dienos vidurkius
# Pajamu ir islaidu santyki procentaliai
# Pajamu ketvircio rezultatus
# Pusmecio islaidu rezultatus

import logging
from datetime import date

ACCOUNTING_FILE = "accounting.txt"

logging.basicConfig(filename='accounting_logs.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


class Accountant:
    def monthly_average(self, amount: float) -> float:
        logging.info(f"Receive amount of monthly average calculations: {amount}")
        return amount / 12

    def daily_average(self, amount: float) -> float:
        return amount / 365

    def calculate_ratio(self, income: float, expenses: float) -> float:
        return round(income / expenses, 2)


class Income(Accountant):
    def __init__(self, income: float):
        self.income = income

    def quarter_income(self) -> float:
        return self.income / 4


class Expenses(Accountant):
    def __init__(self, expenses: float) -> None:
        self.expenses = expenses

    def half_year_expenses(self) -> float:
        return self.expenses / 2


def main() -> None:
    income = float(input("Enter your yearly income: "))
    expenses = float(input("Enter your yearly expenses: "))
    logging.info(f"Income amount {income} ")
    logging.info(f"Expenses amount {expenses} ")
    inc = Income(income)
    exp = Expenses(expenses)
    write_information_to_file(f""" 
Accounting year: {date.today().year} 
    
Our yearly income: ${income},
Our yearly expenses: ${expenses},
Our quarterly income: ${inc.quarter_income()}, 
Our daily expenses: ${round(exp.daily_average(expenses), 2)}.
\n""")

def write_information_to_file(data: str) -> None:
    with open(ACCOUNTING_FILE, 'a') as f:
        f.write(data)

if __name__ == "__main__":
    main()