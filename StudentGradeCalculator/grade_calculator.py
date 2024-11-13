def getStudentInfo():
    name = input("Enter the student's name: ")
    scores = list(map(float, input("Enter the grades through the space: ").split()))
    return name, scores

def calculateAverage(scores):
    return sum(scores) / len(scores)

def assignGrade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def displayResults(name, average, grade):
    print(f"Student: {name}")
    print(f"Grade Point Average: {average}")
    print(f"Evaluation: {grade}")

def main():
    name, scores = getStudentInfo()
    average = calculateAverage(scores)
    grade = assignGrade(average)
    displayResults(name, average, grade)

if __name__ == "__main__":
    main()
