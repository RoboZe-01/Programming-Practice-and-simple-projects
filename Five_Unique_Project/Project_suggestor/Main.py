
# I am currently working on the input part of the project
# it is basic testing of the program  






focus = input("Specify your area of interest : ")
involve = input("Specify technologies or libraries : ")
dificulty_level = input("Enter the difficulty level you want : (Easy / Medium / Hard ) : ")
goal = input("Specify if you're looking for projects with a well-defined outcome : ")
learning = input("Specify your learning goals, e.g., beginners, intermediate learners, portfolio projects, personal projects")
functionalities = input("Specify any specific features or functionalities, e.g., real-time data processing, image recognition, natural language processing : ")
goal = input("Specify if you're looking for projects with a well-defined outcome, e.g., building a web application, training a model, creating a game : ")

final_prompt =f"""

Find me Python projects that:

* **Focus on:** {focus}
* **Involve:** {involve}
* **Difficulty Level:** {dificulty_level}
* **Have a clear goal:** {goal}
* **Are suitable for:** {learning}
* **Incorporate:** {functionalities}

Provide a list of 5-10 project ideas with brief descriptions and links to relevant tutorials or resources if available."""


print(final_prompt)


# Thus a simple promt is generated 