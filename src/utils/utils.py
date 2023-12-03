import random

def randomUniqueChoices(population, weights, k):
    selectedSet = set()
    while len(selectedSet) < k:
        choices = random.choices(population, weights, k=k - len(selectedSet))
        selectedSet.update(choices)
    return list(selectedSet)