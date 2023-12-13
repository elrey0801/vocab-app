import random

def randomUniqueChoices(population, weights, k):
    selectedSet = set()
    while len(selectedSet) < k:
        choices = random.choices(population, weights, k=k - len(selectedSet))
        selectedSet.update(choices)
    return list(selectedSet)

def makeOptions(setOfMeaning, thisMeaning):
    copyOfSetOfMeaning = setOfMeaning.copy()
    copyOfSetOfMeaning.discard(thisMeaning)
    randomOption = random.sample(sorted(copyOfSetOfMeaning), 3)
    randomOption.append(thisMeaning)
    random.shuffle(randomOption)
    return randomOption