import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from .scripts import movies_query as m
from .scripts import credits_query as c