import bloomdata_rebeccatsang.helper__functions2 as hf 

adjectives = ['badass', 'delirious', 'mindnumbing', 'nuclear']
nouns = ['butt', 'bread', 'sloth', 'fart', 'face']

list1 = [1, 2, 3]
list2 = [4, 5, 6]

def test_random_phrase():

    # Listing out every single combo is too time-consuming
    assert type(hf.random_phrase(adjectives, nouns)) == str

    assert type(hf.random_phrase(list1, list2)) == str
    
