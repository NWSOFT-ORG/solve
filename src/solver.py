from multipledispatch import dispatch
from sympy import Eq, init_printing, parse_expr, pprint, pretty, solve, Symbol

init_printing(use_unicode=True)


def find_symbol(eq: str):
    symbols = []
    for char in eq:
        if char not in "0123456789+-*/^%&.":
            symbols.append(char)

    symbols = list(set(symbols))  # Remove duplicates
    if len(symbols) > 1:
        var = input("Enter the unknown variable: ")
        return var
    elif len(symbols) == 0:
        print("Error: No unknown variable")
    else:
        return symbols[0]


@dispatch(str, float)
def solve_equation(eq: str, equals: float):
    expr = parse_expr(eq)
    unknown = find_symbol(eq)
    try:
        x = Symbol(unknown)
    except (SyntaxError, TypeError, ValueError):
        print("Error: Invalid equation")
        return []

    equation = Eq(expr, equals)
    pprint(equation, use_unicode=True)

    try:
        return solve(equation, x)
    except NotImplementedError:
        print("Error: Cannot solve this equation")
        return []


@dispatch(str, str, float)
def solve_equation(unknown: str, eq: str, equals: float):
    try:
        expr = parse_expr(eq)
    except (SyntaxError, TypeError, ValueError):
        print("Error: Invalid equation")
        return []

    x = Symbol(unknown)
    equation = Eq(expr, equals)
    print(f"Simplified Equation: {'-' * 20}")
    pprint(equation, use_unicode=True)
    print(f"---------------------{'-' * 20}")

    try:
        return solve(equation, x)
    except NotImplementedError:
        print("Error: Cannot solve this equation")
        return []


def print_res(unknown: str, res: list):
    if len(res) == 0:
        print("=> No solution")
    else:
        print(f"=> Total {len(res)} solution{'s' if len(res) > 1 else ''}")
        print("=>    \n", end="")
        for i, r in enumerate(res):
            print(f"{unknown} =\n{pretty(r)}\n", end="")
            if i != len(res) - 1:
                print("=> or ", end="")


if __name__ == "__main__":
    print_res("y", solve_equation("y**4", 4.0))
