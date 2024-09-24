#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime


class Payment:
    def __init__(self, surname, name, patronymic, salary, 
                 year_of_employment, bonus_percentage, income_tax, work_days,
                 working_days):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.salary = float(salary)
        self.year_of_employment = int(year_of_employment)
        self.bonus_percentage = float(bonus_percentage)
        self.income_tax = float(income_tax)
        self.work_days = int(work_days)
        self.working_days = int(working_days)
        self.accrued_amount = 0.0
        self.deducted_amount = 0.0

    def read(self, prompt=None):
        line = input() if prompt is None else input(prompt)
        parts = line.split()

        if len(parts) != 9:
            raise ValueError("Введите все необходимые значения")

        self.surname = parts[0]
        self.name = parts[1]
        self.patronymic = parts[2]
        self.salary = float(parts[3])
        self.year_of_employment = int(parts[4])
        self.bonus_percentage = float(parts[5])
        self.income_tax = float(parts[6])
        self.work_days = int(parts[7])
        self.working_days = int(parts[8])

    def display(self):
        print(
            f"Фамилия: {self.surname}, Имя: {self.name}, Отчество: {self.patronymic}")
        print(
            f"Оклад: {self.salary}, Год поступления на работу: {self.year_of_employment}")
        print(
            f"Процент надбавки: {self.bonus_percentage}, Подоходный налог: {self.income_tax}")
        print(
            f"Отработанные дни: {self.work_days}, Рабочие дни: {self.working_days}")
        print(
            f"Начисленная сумма: {self.accrued_amount}, Удержанная сумма: {self.deducted_amount}")

    def calculate_accrued_amount(self):
        base_amount = self.salary / self.working_days * self.work_days
        bonus_amount = base_amount * (self.bonus_percentage / 100)
        self.accrued_amount = base_amount + bonus_amount
        return self.accrued_amount

    def calculate_deducted_amount(self):
        pension_fund_deduction = self.accrued_amount * 0.01
        income_tax_deduction = (
            self.accrued_amount - pension_fund_deduction) * (self.income_tax / 100)
        self.deducted_amount = pension_fund_deduction + income_tax_deduction
        return self.deducted_amount

    def calculate_net_amount(self):
        return self.accrued_amount - self.deducted_amount

    def calculate_experience(self):
        current_year = datetime.now().year
        return current_year - self.year_of_employment


if __name__ == '__main__':
    p1 = Payment("Иванов", "Иван", "Иванович", 50000, 2015, 10, 13, 20, 22)
    p1.display()
    print(f"Начисленная сумма: {p1.calculate_accrued_amount()}")
    print(f"Удержанная сумма: {p1.calculate_deducted_amount()}")
    print(f"Сумма на руки: {p1.calculate_net_amount()}")
    print(f"Стаж: {p1.calculate_experience()} лет")

    p2 = Payment("", "", "", 0, 0, 0, 0, 0, 0)
    p2.read("Введите фамилию, имя, отчество, оклад, год поступления, процент надбавки, подоходный налог, отработанные дни, рабочие дни: ")
    p2.display()
    print(f"Начисленная сумма: {p2.calculate_accrued_amount()}")
    print(f"Удержанная сумма: {p2.calculate_deducted_amount()}")
    print(f"Сумма на руки: {p2.calculate_net_amount()}")
    print(f"Стаж: {p2.calculate_experience()} лет")
