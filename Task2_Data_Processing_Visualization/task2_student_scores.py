import requests
import matplotlib.pyplot as plt


API_URL = "https://api.slingacademy.com/v1/sample-data/files/student-scores.json"

response = requests.get(API_URL)

if response.status_code == 200:
    data = response.json()

    students = data

    # Display first 10 students and their math scores
    print("First 10 Students and Their Math Scores")
    print("-" * 40)

    for student in students[:10]:
        name = student["first_name"] + " " + student["last_name"]
        score = student["math_score"]

        print("Name:", name)
        print("Math Score:", score)
        print("-" * 40)

    # Calculate average math score of all students
    scores = []

    for student in students:
        scores.append(student["math_score"])

    average_score = sum(scores) / len(scores)

    print("\nAverage Math Score:", round(average_score, 2))

    # Graphical representation
    # Prepare data for the bar chart
    names = []
    scores_for_chart = []

    for student in students[:10]:
        name = student["first_name"] + " " + student["last_name"]
        score = student["math_score"]

        names.append(name)
        scores_for_chart.append(score)

    # Create bar chart
    plt.bar(names, scores_for_chart)

    plt.xlabel("Students")
    plt.ylabel("Math Score")
    plt.title("Math Scores of First 10 Students")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()

else:
    print("Failed to fetch data")