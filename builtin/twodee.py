import os
from contextlib import contextmanager
import sys, os

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout
os.system("pip install pygame -q>NUL")
with suppress_stdout():
    print("importing lol")
    import pygame as engine

