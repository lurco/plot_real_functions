import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="darkgrid")


def plot_function(*funcs, x_start, x_end, label="f(x)", size=(12, 8)):
    x = np.linspace(x_start, x_end, 100)
    fig, ax = plt.subplots(figsize=size)
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.spines["top"].set_color("none")
    ax.spines["right"].set_color("none")
    ax.xaxis.set_ticks_position("bottom")
    ax.yaxis.set_ticks_position("left")
    ax.set_xlabel("x", fontsize=12, labelpad=15)
    ax.set_ylabel("y", fontsize=12, labelpad=15, rotation=0)
    ax.yaxis.set_label_coords(0.52, 0.95)
    ax.xaxis.set_label_coords(0.97, 0.55)
    ax.hlines(0, x_start, x_end, color="black", linewidth=2)
    for f in funcs:
        ax.plot(x, f(x), label=label)
    y_min, y_max = ax.get_ylim()
    ax.vlines(
        0,
        y_min,
        y_max,
        color="black",
        linewidth=2,
    )
    plt.show()
