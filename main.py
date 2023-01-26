"""
Solve 0.1
Licensed under GPL 3.0, by Andy Zhang
"""
from src.interface import ask_equation, expand, welcome
from src.solver import find_symbol, print_res, solve_equation


def solve():
    welcome()
    while True:
        s = ask_equation()
        if s == "exit":
            break
        equation = expand(s)
        lhs = equation[0]
        rhs = equation[1]
        if lhs is None or rhs is None:
            print("Error: Invalid equation")
            continue
        symbol = find_symbol(lhs)

        try:
            print_res(symbol, solve_equation(symbol, lhs, float(rhs)))
        except ValueError:
            print("Error: Invalid equation")
            continue


if __name__ == "__main__":
    solve()
