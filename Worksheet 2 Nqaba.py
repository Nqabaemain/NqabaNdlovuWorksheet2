# Creating a list of courses in any order
courses = [
    "Introduction to Programming",
    "Calculus I",
    "Data Structures and Algorithms",
    "Linear Algebra",
    "Physics I",
    "Chemistry I",
    "Biology I",
    "Microeconomics",
    "Macroeconomics",
    "Psychology I",
    "History I",
    "English Composition I",
    "Introduction to Philosophy",
    "Calculus II",
    "Discrete Mathematics"
]

# Printing the list in its original order
print("Original list:")
print(courses)
# Sorting the list alphabetically
sorted_courses = sorted(courses)

# Printing the sorted list
print("\nSorted list (alphabetically):")
print(sorted_courses)

# Sorting the list in reverse alphabetical order
reverse_sorted_courses = sorted(courses, reverse=True)

# Printing the reverse sorted list
print("\nSorted list (reverse alphabetical):")
print(reverse_sorted_courses)

# Reversing the order of the list
courses.reverse()

# Printing the reversed list
print("\nReversed list:")
print(courses)

# Reversing the order of the list again to return to the original order
courses.reverse()

# Printing the list to verify it is back to its original order
print("\nReversed back to original order:")
print(courses)

# Sorting the list alphabetically in place
courses.sort()

# Printing the sorted list
print("\nSorted list (alphabetically) in place:")
print(courses)

# Sorting the list in reverse alphabetical order in place
courses.sort(reverse=True)

# Printing the reverse sorted list
print("\nSorted list (reverse alphabetical) in place:")
print(courses)

# Initial unordered list of courses
courses = [
    "Calculus I",
    "Biology I",
    "Introduction to Programming",
    "Physics I",
    "Data Structures and Algorithms",
    "Chemistry I",
    "English Composition I",
    "Discrete Mathematics",
    "History I",
    "Macroeconomics",
    "Microeconomics",
    "Introduction to Philosophy",
    "Calculus II",
    "Linear Algebra",
    "Psychology I"
]

# Creating a sorted list without modifying the original list
sorted_courses = sorted(courses)

# Print announcement message
print("The following courses are available for expression of interest if the students meet the prerequisites:")

# Print sorted list
for course in sorted_courses:
    print(course)

    # Original list
    original_courses = [
        "Calculus I",
        "Biology I",
        "Introduction to Programming",
        "Physics I",
        "Data Structures and Algorithms",
        "Chemistry I",
        "English Composition I",
        "Discrete Mathematics",
        "History I",
        "Macroeconomics",
        "Microeconomics",
        "Introduction to Philosophy",
        "Calculus II",
        "Linear Algebra",
        "Psychology I"
    ]
    # Replacing "Chemistry I" with "Physics I"
    updated_courses = [course if course != "Chemistry I" else "Physics I" for course in original_courses]

    # Print the course change message
    print("\nCourse withdrawal and replacement:")
    print(f"The course 'Chemistry I' has been withdrawn.")
    print(f"The new course 'Physics I' is now available.")

    # Updated courses list with the original and the new course
    updated_courses = [
        "Calculus I",
        "Biology I",
        "Introduction to Programming",
        "Physics I",
        "Data Structures and Algorithms",
        "Physics I",
        "English Composition I",
        "Discrete Mathematics",
        "History I",
        "Macroeconomics",
        "Microeconomics",
        "Introduction to Philosophy",
        "Calculus II",
        "Linear Algebra",
        "Psychology I"
    ]

    # New courses to add
    new_courses = ["Astronomy", "Advanced Calculus", "Machine Learning"]

    # Adding new courses using insert() and append()
    updated_courses.insert(0, new_courses[0])  # Add to the beginning
    updated_courses.insert(len(updated_courses) // 2, new_courses[1])  # Add to the middle
    updated_courses.append(new_courses[2])  # Add to the end

    # Print the updated list
    print("\nUpdated list with new courses:")
    for course in updated_courses:
        print(course)

        # Remove specific courses
        courses_to_remove = ["Data Structures and Algorithms", "Physics I", "Macroeconomics", "Advanced Calculus"]

        # Inform students about the removed courses
        print("\nCourses unavailable due to technical and room availability issues:")
        for course in courses_to_remove:
            print(course)

        # Remove the courses one by one using pop()
        for course in courses_to_remove:
            if course in updated_courses:
                updated_courses.remove(course)

        # Print the updated list
        print("\nUpdated list with available courses:")
        for course in updated_courses:
            print(course)

            # Define the list of tuples with course_id and course_name
            courses_tuples = [
                (1, "Introduction to Programming"),
                (2, "Calculus I"),
                (3, "Data Structures and Algorithms"),
                (4, "Linear Algebra"),
                (5, "Physics I"),
                (6, "Chemistry I"),
                (7, "Biology I"),
                (8, "Microeconomics"),
                (9, "Macroeconomics"),
                (10, "Psychology I"),
                (11, "History I"),
                (12, "English Composition I"),
                (13, "Introduction to Philosophy"),
                (14, "Calculus II"),
                (15, "Discrete Mathematics")
            ]

            # Create an empty list to store course names
            course_names = []

            # Loop through each tuple in the list
            for course_id, course_name in courses_tuples:
                # Add the course name to the list
                course_names.append(course_name)

                # Print the course names
                print("Course names extracted from the tuples:")
                for name in course_names:
                    print(name)

                    # Define the list of tuples with course_id and course_name
                    courses_tuples = [
                        (1, "Introduction to Programming"),
                        (2, "Calculus I"),
                        (3, "Data Structures and Algorithms"),
                        (4, "Linear Algebra"),
                        (5, "Physics I"),
                        (6, "Chemistry I"),
                        (7, "Biology I"),
                        (8, "Microeconomics"),
                        (9, "Macroeconomics"),
                        (10, "Psychology I"),
                        (11, "History I"),
                        (12, "English Composition I"),
                        (13, "Introduction to Philosophy"),
                        (14, "Calculus II"),
                        (15, "Discrete Mathematics")
                    ]

                    # Create an empty list to store course names
                    course_names = []

                    # Loop through each tuple in the list
                    for course_id, course_name in courses_tuples:
                        # Add the course name to the list
                        course_names.append(course_name)

                    # Print the course names
                    print("Course names extracted from the tuples:")
                    for name in course_names:
                        print(name)

                        # Define the list of tuples with course_id and department
                        course_departments = [
                            (1, "Computer Science"),
                            (2, "Mathematics"),
                            (3, "Computer Science"),
                            (4, "Mathematics"),
                            (5, "Physics"),
                            (6, "Chemistry"),
                            (7, "Biology"),
                            (8, "Economics"),
                            (9, "Economics"),
                            (10, "Psychology"),
                            (11, "History"),
                            (12, "English"),
                            (13, "Philosophy"),
                            (14, "Mathematics"),
                            (15, "Computer Science")
                        ]


                        def find_department(course_id):
                            # Iterate through the list of tuples
                            for cid, department in course_departments:
                                if cid == course_id:
                                    return department
                            return "Course ID not found"  # Return this if the course ID is not in the list


                        # Example course ID to search
                        search_id = 10

                        # Find the department for the given course ID
                        department = find_department(search_id)

                        # Print the result using conditional statements
                        if department == "Course ID not found":
                            print(f"The course ID {search_id} is not available in the list.")
                        else:
                            print(f"The department for course ID {search_id} is {department}.")

                            # Define the list of tuples with course_id, course_name, department, and prerequisites
                            courses_info = [
                                [1, "Introduction to Programming", "Computer Science", "None"],
                                [2, "Calculus I", "Mathematics", "None"],
                                [3, "Data Structures and Algorithms", "Computer Science",
                                 "Introduction to Programming"],
                                [4, "Linear Algebra", "Mathematics", "None"],
                                [5, "Physics I", "Physics", "None"],
                                [6, "Chemistry I", "Chemistry", "None"],
                                [7, "Biology I", "Biology", "None"],
                                [8, "Microeconomics", "Economics", "None"],
                                [9, "Macroeconomics", "Economics", "Microeconomics"],
                                [10, "Psychology I", "Psychology", "None"],
                                [11, "History I", "History", "None"],
                                [12, "English Composition I", "English", "None"],
                                [13, "Introduction to Philosophy", "Philosophy", "None"],
                                [14, "Calculus II", "Mathematics", "Calculus I"],
                                [15, "Discrete Mathematics", "Computer Science", "Introduction to Programming"]
                            ]


                            # Function to find department by course_id
                            def find_department(course_id):
                                for course in courses_info:
                                    if course[0] == course_id:
                                        return course[2]  # Return the department
                                return None  # Return None if not found


                            # Function to retrieve course information by course_id
                            def get_course_info(course_id):
                                for course in courses_info:
                                    if course[0] == course_id:
                                        return {
                                            "Course Name": course[1],
                                            "Department": course[2],
                                            "Prerequisites": course[3]
                                        }
                                return None  # Return None if not found


                            # Infinite loop until user decides to quit
                            while True:
                                user_input = input("Enter a course ID (1-15), '0', or 'quit' to exit: ").strip()

                                # Conditional handling of user input
                                if user_input.lower() in ['0', 'quit']:
                                    print("Exiting the system. Goodbye!")
                                    break
                                else:
                                    try:
                                        course_id = int(user_input)
                                        if 1 <= course_id <= 15:
                                            department = find_department(course_id)
                                            if department:
                                                print(f"Course ID {course_id} is in the {department} department.")
                                            else:
                                                print(f"Course ID {course_id} is not found in the list.")
                                        else:
                                            print(f"Course ID {course_id} is out of range (1-15), try again.")
                                    except ValueError:
                                        print(f"The value '{user_input}' has been used to exit.")

                            # Prompt user to enter a course ID and display course details
                            while True:
                                try:
                                    course_id = int(input("Enter a course ID to retrieve course information (1-15): "))
                                    if 1 <= course_id <= 15:
                                        course_info = get_course_info(course_id)
                                        if course_info:
                                            print(f"Course Information for ID {course_id}:")
                                            print(f"Course Name: {course_info['Course Name']}")
                                            print(f"Department: {course_info['Department']}")
                                            print(f"Prerequisites: {course_info['Prerequisites']}")
                                        else:
                                            print(f"Course ID {course_id} is not found in the list.")
                                    else:
                                        print("Course ID is out of range (1-15). Try again.")
                                except ValueError:
                                    print("Invalid input. Please enter a valid course ID.")

                                    # Define the list of tuples with course_id, course_name, department, and prerequisites
                                    courses_info = [
                                        [1, "Introduction to Programming", "Computer Science", "None"],
                                        [2, "Calculus I", "Mathematics", "None"],
                                        [3, "Data Structures and Algorithms", "Computer Science",
                                         "Introduction to Programming"],
                                        [4, "Linear Algebra", "Mathematics", "None"],
                                        [5, "Physics I", "Physics", "None"],
                                        [6, "Chemistry I", "Chemistry", "None"],
                                        [7, "Biology I", "Biology", "None"],
                                        [8, "Microeconomics", "Economics", "None"],
                                        [9, "Macroeconomics", "Economics", "Microeconomics"],
                                        [10, "Psychology I", "Psychology", "None"],
                                        [11, "History I", "History", "None"],
                                        [12, "English Composition I", "English", "None"],
                                        [13, "Introduction to Philosophy", "Philosophy", "None"],
                                        [14, "Calculus II", "Mathematics", "Calculus I"],
                                        [15, "Discrete Mathematics", "Computer Science", "Introduction to Programming"]
                                    ]


                                    # Function to find course information by course_id
                                    def get_course_info(course_id):
                                        # Iterate through the list of tuples
                                        for course in courses_info:
                                            if course[0] == course_id:
                                                return {
                                                    "Course Name": course[1],
                                                    "Department": course[2],
                                                    "Prerequisites": course[3]
                                                }
                                        return None  # Return None if course_id is not found


                                    # Infinite loop for user interaction
                                    while True:
                                        user_input = input("Enter a course ID (1-15), '0', or 'quit' to exit: ").strip()

                                        # Conditional handling of user input
                                        if user_input.lower() in ['0', 'quit']:
                                            print("Exiting the system. Goodbye!")
                                            break
                                        else:
                                            # Input validation for course ID
                                            try:
                                                course_id = int(user_input)
                                                if 1 <= course_id <= 15:
                                                    # Retrieve course information
                                                    course_info = get_course_info(course_id)
                                                    if course_info:
                                                        print(f"Course Information for ID {course_id}:")
                                                        print(f"Course Name: {course_info['Course Name']}")
                                                        print(f"Department: {course_info['Department']}")
                                                        print(f"Prerequisites: {course_info['Prerequisites']}")
                                                    else:
                                                        print(f"Course ID {course_id} is not found in the list.")
                                                else:
                                                    print(
                                                        "Course ID is out of range (1-15). Please enter a valid course ID.")
                                            except ValueError:
                                                print("Invalid input. Please enter a valid integer for the course ID.")


