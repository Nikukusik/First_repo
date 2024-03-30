import re
from typing import Callable

def generator_numbers(text):
    pattern = "\d+.\d+"
    salary = re.findall(pattern, text)
    for i in salary:
        yield i
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 i 324.00 доларів."
#for num in generator_numbers(text):
#    print(float(num))

def sum_profit(text, func: Callable):
    sum = float(0)
    for num in func(text):
        sum += float(num)
    return sum

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")