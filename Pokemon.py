import random
from abc import ABC, abstractmethod


class AnimeMon(ABC):

    @classmethod
    @abstractmethod
    def inc_exp(self, value: int):
        return


class Pokemon(AnimeMon):
    def __init__(self, name: str, poketype: str):
        self.name = name
        self.poketype = poketype
        self.exp = 0

    def __str__(self):
        return f'{self.name}/{self.poketype}'

    def inc_exp(self, step_size: int):
        self.exp += step_size


class Digimon(AnimeMon):
    def __init__(self, name: str):
        self.name = name
        self.exp = 0

    def inc_exp(self, value: int):
        self.exp += value * 8


def train(pokemon):
    step_size, level_size = 10, 100
    sparring_qty = (level_size - pokemon.exp % level_size) // step_size
    for i in range(sparring_qty):
        win = random.choice([True, False])
        if win:
            pokemon.inc_exp(step_size)


if __name__ == '__main__':
    # bulbasaur = Pokemon(name='Bulbasaur', poketype='grass')
    # train(bulbasaur)
    # print(bulbasaur.exp)
    agumon = Digimon(name='Agumon')
    train(agumon)
    print(agumon.exp)

