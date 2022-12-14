"""
author: Tanner Levi
"""

from sentences import get_determiner, get_noun, get_verb,\
     get_preposition, get_prepositional_phrase
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    # 1. Test the singular nouns:
    single_nouns = ["bird", "boy", "car", "cat", "child", \
            "dog", "girl", "man", "rabbit", "woman"]
    
    # This loop will repeat the statements inside it 10 times.
    for _ in range(10):

        # Call the get_noun function which should return
        # a singular noun
        noun = get_noun(1)

        # Verify that the noun returned from get_noun function
        # is one of the nouns in the single_nouns list.
        assert noun in single_nouns

    # 2. Test the plural nouns:
    plural_nouns = ["birds", "boys", "cars", "cats", "children",\
            "dogs", "girls", "men", "rabbits", "women"]
    
    # This loop will repeat the statements inside it 10 times.
    for _ in range(10):

        # Call the get_noun function which should return
        # a plural noun
        noun = get_noun(2)

        # Verify that the noun returned from get_noun function
        # is one of the nouns in the plural_nouns list
        assert noun in plural_nouns

def test_get_verb():
    # 1. Test the past tense verbs
    past_verbs = ["drank", "ate", "grew", "laughed", "thought",\
            "ran", "slept", "talked", "walked", "wrote"]
    
    # This loop will repeat 5 times.
    for _ in range(5):

        # Call the get_verb function which should return
        # a past tense verb
        verb = get_verb(1, 'past')

        # Verify that the returned verb is on the list
        assert verb in past_verbs
    
    # 2. Test the singular present tense verbs
    present_singular_verbs = ["drinks", "eats", "grows", "laughs", "thinks",\
            "runs", "sleeps", "talks", "walks", "writes"]

    # Repeats 5 times.
    for _ in range(5):

        # Call the get_verb function to return a present singular verb
        verb = get_verb(1, 'present')

        # Verify the returned verb is on the list
        assert verb in present_singular_verbs
    
    # 3. Test the plural present tense verbs
    present_plural_verbs = ["drink", "eat", "grow", "laugh", "think",\
            "run", "sleep", "talk", "walk", "write"]
        
    # repeats 5 times.
    for _ in range(5):

        # Call get_verb function to return present plural verb
        verb = get_verb(2, 'present')

        # Verify the returned verb is on the list
        assert verb in present_plural_verbs

    # 4. Test the future tense verbs
    future_verbs = ["will drink", "will eat", "will grow", "will laugh",\
            "will think", "will run", "will sleep", "will talk",\
                "will walk", "will write"]
    
    # repeats 5 times.
    for _ in range(5):

        # Call get_verb function to return future verb
        verb = get_verb(1, 'future')

        # Verify the returned verb is on the list
        assert verb in future_verbs

def test_get_preposition():
    # 1. Test the prepositions
    preps = ["about", "above", "across", "after", "along",\
        "around", "at", "before", "behind", "below",\
            "beyond", "by", "despite", "except", "for",\
                "from", "in", "into", "near", "of",\
                    "off", "on", "onto", "out", "over",\
                        "past", "to", "under", "with", "without"]
    
    # repeats 5 times.
    for _ in range(5):

        # Call get_preposition function to return a preposition
        prep = get_preposition()

        # Verify that prep is on the list
        assert prep in preps

def test_get_prepositional_phrase():
    # 1. Test that the prepositional phrase has the correct quantity
    single_determiners = ["a", "one", "the"]

    plural_determiners = ["some", "many", "the"]

    single_nouns = ["bird", "boy", "car", "cat", "child", \
            "dog", "girl", "man", "rabbit", "woman"]
 
    plural_nouns = ["birds", "boys", "cars", "cats", "children",\
            "dogs", "girls", "men", "rabbits", "women"]

    prepositions = ["about", "above", "across", "after", "along",\
    "around", "at", "before", "behind", "below",\
        "beyond", "by", "despite", "except", "for",\
            "from", "in", "into", "near", "of",\
                "off", "on", "onto", "out", "over",\
                    "past", "to", "under", "with", "without"]

    # repeats 10 times
    for _ in range(10):

        # Call get_prepositional_phrase to return single and plural
        prep = get_prepositional_phrase(1)
        preps = get_prepositional_phrase(2)

        # Verify that the length of the list 3
        assert len(prep) == 3
        assert len(preps) == 3

        # Verify that the singular and plural parts are in the lists
        assert prep[0] in prepositions
        assert prep[1] in single_determiners
        assert prep[2] in single_nouns

        assert preps[0] in prepositions
        assert preps[1] in plural_determiners
        assert preps[2] in plural_nouns

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])