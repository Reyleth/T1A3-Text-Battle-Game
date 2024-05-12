import sys
sys.path.append('src')

from weapons import rusty_sword
from battle import battle
from character import Character, Hero, Enemy


def test_battle_hero_wins(mocker):
    mocker.patch('builtins.input', return_value='1')
    hero = Hero(name="Hero", progress=1, gold=0, inventory=[rusty_sword])
    assert battle(hero) is True

def test_battle_hero_loses(mocker):
    mocker.patch('builtins.input', return_value='1')
    hero = Hero(name="Hero", progress=1, gold=0, inventory=[])
    assert battle(hero) is False

def test_battle_hero_runs(mocker):
    mocker.patch('builtins.input', return_value='3')
    hero = Hero(name="Hero", progress=1, gold=0, inventory=[])
    assert battle(hero) is None
