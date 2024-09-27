import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from IPython.display import HTML


class Funkcja:
    def __init__(self, wzor):
        self.wzor = wzor

    def parse_into_latex(self):
        return (
            self.wzor.replace("**", "^")
            .replace("*", "")
            .replace("/", " / ")
            .replace("+", " + ")
            .replace("-", " - ")
        )

    # wzor = "x**2 + 2*x + 1"
    # f = Funkcja(wzor)
    # print(f.oblicz(2))

    def wartosc_dla(self, x):
        try:
            return eval(self.wzor, {"x": x})
        except ZeroDivisionError:
            return 0

    def wykres(self, x_poczatek, x_koniec):
        """
        Funkcja rysująca wykres funkcji
        z przerywaną linią dla oznaczenia osi x i y przecinających się w punkcie (0,0),
        i z zachowaniem proporcji 1:1
        """
        x = np.linspace(x_poczatek, x_koniec, 100)
        y = [self.wartosc_dla(i) for i in x]
        plt.plot(x, y)
        plt.axhline(0, color="black", linestyle="--")
        plt.axvline(0, color="black", linestyle="--")
        plt.gca().set_aspect("equal", adjustable="box")
        plt.show()

    def tabela(self, x_poczatek, x_koniec, krok=1):
        x = np.arange(x_poczatek, x_koniec, krok)
        y = [self.wartosc_dla(i) for i in x]
        df = pd.DataFrame({"x": x, "y": y})
        return HTML(df.T.to_html(header=False))

    def __add__(self, other_function):
        if isinstance(other_function, Funkcja):
            return Funkcja(f"{self.wzor} + {other_function.wzor}")
        elif isinstance(other_function, (int, float)):
            return Funkcja(f"{self.wzor} + {other_function}")

    def __sub__(self, other_function):
        if isinstance(other_function, Funkcja):
            return Funkcja(f"{self.wzor} - {other_function.wzor}")
        elif isinstance(other_function, (int, float)):
            return Funkcja(f"{self.wzor} - {other_function}")

    def __mul__(self, other_function):
        if isinstance(other_function, Funkcja):
            return Funkcja(f"({self.wzor}) * ({other_function.wzor})")
        elif isinstance(other_function, (int, float)):
            return Funkcja(f"({self.wzor}) * ({other_function})")

    def __truediv__(self, other_function):
        if isinstance(other_function, Funkcja):
            return Funkcja(f"({self.wzor}) / ({other_function.wzor})")
        elif isinstance(other_function, (int, float)):
            return Funkcja(f"({self.wzor}) / ({other_function})")

    def __pow__(self, other_function):
        if isinstance(other_function, Funkcja):
            return Funkcja(f"({self.wzor}) ** ({other_function.wzor})")
        elif isinstance(other_function, (int, float)):
            return Funkcja(f"({self.wzor}) ** ({other_function})")

    def __str__(self):
        return self.wzor


def Wykres(x_poczatek, x_koniec, *args):
    """
    Funkcja rysująca wykresy funkcji
    z przerywaną linią dla oznaczenia osi x i y przecinających się w punkcie (0,0),
    i z zachowaniem proporcji 1:1
    """
    for arg in args:
        x = np.linspace(x_poczatek, x_koniec, 100)
        y = [arg.wartosc_dla(i) for i in x]
        plt.plot(x, y, label=arg.wzor)
    plt.axhline(0, color="black", linestyle="--")
    plt.axvline(0, color="black", linestyle="--")
    plt.gca().set_aspect("equal", adjustable="box")
    plt.legend()
    plt.show()
