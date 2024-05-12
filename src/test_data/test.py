'''Module for testing battle function'''
import sys
sys.path.append('src')

from weapons import rusty_sword
from battle import battle
from character import Hero

# Test goblin battle
def test_battle_hero_wins(mocker):
    '''Test battle function with hero winning'''
    mocker.patch('builtins.input', return_value='1')
    hero = Hero(name="Hero", progress=1, gold=0, inventory=[rusty_sword])
    assert battle(hero) is True

# Test giant spider battle, lose expected
def test_battle_hero_loses(mocker):
    '''Test battle function with hero losing'''
    mocker.patch('builtins.input', return_value='1')
    hero = Hero(name="Hero", progress=5, gold=0, inventory=[rusty_sword])
    assert battle(hero) is False

# Test hero runs from battle
def test_battle_hero_runs(mocker):
    '''Test battle function with hero returning '''
    mocker.patch('builtins.input', return_value='3')
    hero = Hero(name="Hero", progress=1, gold=0, inventory=[])
    assert battle(hero) is None
