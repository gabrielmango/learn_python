from collections import namedtuple
from typing import NamedTuple

Cart = namedtuple('Cart', ['value', 'type'])

ace_of_spades = Cart('A', 'spades')

for value in ace_of_spades:
    print(value)

class Cart(NamedTuple):
    value: str = 'VALUE'
    type: str = 'TYPE'

king_of_swords = Cart('king', 'swords')

for value in king_of_swords:
    print(value)