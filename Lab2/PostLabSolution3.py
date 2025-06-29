# Program: generator.py
# Author: Ken (modified)
# Generates and displays sentences using a simple grammar
# and vocabulary. Words are chosen at random from external text files.

import random

def getWords(filename):
    """Reads words from a file and returns them as a tuple."""
    with open(filename, "r") as file:
        words = [line.strip().upper() for line in file if line.strip()]
    return tuple(words)

# Load vocabulary from text files
articles = getWords("articles.txt")
nouns = getWords("nouns.txt")
verbs = getWords("verbs.txt")
prepositions = getWords("prepositions.txt")

def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounPhrase() + " " + \
           prepositionalPhrase()

def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    """Prompts the user for the number of sentences to generate."""
    number = int(input("Enter the number of sentences: "))
    for _ in range(number):
        print(sentence())

if __name__ == "__main__":
    main()
