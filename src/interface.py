def ask_equation() -> str:
    equation = input("eq> ")
    return equation


def expand(equation: str) -> tuple:
    try:
        lhs = equation.split("=")[0]
        rhs = equation.split("=")[1]
    except IndexError:
        return None, None

    return lhs, rhs


def welcome():
    print("SOLVE 0.1")
    print("Licensed under GPL 3.0, by Andy Zhang")
    print("Type \"exit\" to exit")
