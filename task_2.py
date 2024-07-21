import re
from typing import Callable, Iterable

text_for_analysis = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід,\
доповнений додатковими надходженнями 27.45 і 324.00 доларів."


def generator_numbers(text: str) -> Iterable:
    for word in text.split(" "):
        if re.match(r"\d+(?:\.\d+)?", word):
            yield float(word)


def sum_profit(text: str, generator: Callable) -> float:
    total_income = 0
    for number in generator(text):
        total_income += number
    return total_income


print(sum_profit(text_for_analysis, generator_numbers))
