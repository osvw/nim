from nim import Nim
from random import randrange

nim = Nim(randrange(9,15,2))
nim.execute()