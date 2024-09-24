#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Pair:
    def __init__(self, first=0.0, second=0):
        if not isinstance(first, (int, float)) or not isinstance(second, int):
            raise ValueError("Некорректные значения аргументов")

        self.first = float(first)
        self.second = int(second)

    def read(self, prompt=None):
        line = input() if prompt is None else input(prompt)
        parts = line.split()

        if len(parts) != 2:
            raise ValueError("Введите два значения")

        self.first = float(parts[0])
        self.second = int(parts[1])

    def display(self):
        print(f"First: {self.first}, Second: {self.second}")

    def summa(self, work_ddays):
        if work_ddays <= 0:
            raise ValueError(
                "Количество дней в месяце должно быть положительным")

        return self.first / work_ddays * self.second


def make_pair(first, second):
    try:
        return Pair(first, second)
    except ValueError as e:
        print(f"Ошибка: {e}")
        exit(1)


if __name__ == '__main__':
    p1 = make_pair(3000.250, 20)
    p1.display()
    print(f"Summa: {p1.summa(30)}")

    p2 = Pair()
    p2.read("Введите оклад и количество отработанных дней: ")
    p2.display()
    print(f"Summa: {p2.summa(30)}")
