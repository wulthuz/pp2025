# PRACTICAL WORK 1

courses = []
students = []

# input students
numOfStudents = int(input("How many students are there in a class? "))

for i in range(numOfStudents):
    print(f"Student {i + 1}'s information:")
    sid = int(input("Id: "))
    name = input("Name: ")
    dob = input("Dob (dd/mm/yy): ")

    students.append({
        "id": sid,
        "name": name,
        "dob": dob
    })

# input courses 
numOfCourses = int(input("\nHow many courses are there? "))

for j in range(numOfCourses):
    print(f"Course {j + 1}'s information:")
    cid = int(input("Id: "))
    cname = input("Name: ")

    courses.append({
        "id": cid,
        "name": cname,
        "marks": {}   # key = student id, value = mark
    })

# input marks
while True:
    courseSelection = int(
        input(f"\nSelect a course (1–{numOfCourses}, 0 to quit): ")
    )

    if courseSelection == 0:
        break

    course = courses[courseSelection - 1]

    print(f"\nEntering marks for course: {course['name']}")
    for student in students:
        mark = int(input(f"Mark for {student['name']}: "))
        course["marks"][student["id"]] = mark

# menu
while True:
    choice = int(
        input(
            "\n1. List courses\n"
            "2. List students\n"
            "3. Show student marks\n"
            "Other number to quit\n"
            "Your choice: "
        )
    )

    # list courses
    if choice == 1:
        print("\nId".ljust(6), "Name")
        for c in courses:
            print(str(c["id"]).ljust(6), c["name"])

    # list students
    elif choice == 2:
        print("\nId".ljust(6), "Name".ljust(15), "Dob")
        for s in students:
            print(
                str(s["id"]).ljust(6),
                s["name"].ljust(15),
                s["dob"]
            )

    # show marks
    elif choice == 3:
        for c in courses:
            print(f"\nCourse: {c['name']}")
            print("\tId".ljust(6), "Name".ljust(15), "Mark")

            for s in students:
                mark = c["marks"].get(s["id"], "N/A")
                print(
                    "\t",
                    str(s["id"]).ljust(6),
                    s["name"].ljust(15),
                    mark
                )

    else:
        break
