# style.py
import matplotlib.pyplot as plt

def apply_style(xlabel, ylabel, title, grid=True):
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(grid)
