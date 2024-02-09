"""
new helper_functions file just for pytest
"""
import random

adjectives = ['badass', 'delirious', 'mindnumbing', 'nuclear']
nouns = ['butt', 'bread', 'sloth', 'fart', 'face']

def random_phrase(adjectives, nouns):

    adjective = random.choice(adjectives)
    noun = random.choice(nouns)

    return adjective + ' ' + noun


if __name__ == '__main__':
    print(random_phrase(adjectives, nouns))