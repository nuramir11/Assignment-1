import random
from collections import Counter

def rollDice():
    return random.randint(1, 6)

def trackRolls(num_rolls):
    rolls = [rollDice() for _ in range(num_rolls)]
    return rolls

def calculateStatistics(rolls):
    total = sum(rolls)
    average = total / len(rolls)
    frequency = Counter(rolls)
    probability = {num: frequency[num] / len(rolls) for num in range(1, 7)}
    return average, frequency, probability

def main():
    num_rolls = int(input("Enter the number of dice rolls: "))
    rolls = trackRolls(num_rolls)
    average, frequency, probability = calculateStatistics(rolls)
    print("Average result:", average)
    print("The frequency of occurrence of each number:", frequency)
    print("The probability of each number falling out:", probability)

if __name__ == "__main__":
    main()
