from db import connect_db

def add_student():

    conn = connect_db()
    cur = conn.cursor()

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender: ")
    email = input("Enter Email: ")
    phone = int(input("Enter Phone Number: "))
    course = input("Enter Course: ")

    query = """
    INSERT INTO student
    (name, age, gender, email, phone_no, course)
    VALUES (%s,%s,%s,%s,%s,%s)
    """

    cur.execute(
        query,
        (name, age, gender, email, phone, course)
    )

    conn.commit()

    print("Student Added Successfully!")

    cur.close()
    conn.close()


def view_students():

    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM student")

    students = cur.fetchall()

    if students:

        for student in students:

            print("\n" + "="*40)
            print(f"Student ID    : {student[0]}")
            print(f"Name          : {student[1]}")
            print(f"Age           : {student[2]}")
            print(f"Gender        : {student[3]}")
            print(f"Email         : {student[4]}")
            print(f"Phone Number  : {student[5]}")
            print(f"Course        : {student[6]}")
            print(f"Admission Date: {student[7]}")
            print("="*40)

    else:
        print("No Student Records Found!")

    cur.close()
    conn.close()

def search_student():

    conn = connect_db()
    cur = conn.cursor()

    student_id = int(input("Enter Student ID: "))

    cur.execute(
        "SELECT * FROM student WHERE student_id = %s",
        (student_id,)
    )
    name = input("Enter the student name:")
    cur.execute(
        "SELECT * FROM student WHERE name = %s",
        (name,)
    )

    student = cur.fetchone()

    if student:
        print("\nStudent Found")
        print(student)
    else:
        print("Student Not Found")

    cur.close()
    conn.close()

def update_student():

    conn = connect_db()
    cur = conn.cursor()

    student_id = int(input("Enter Student ID: "))
    new_course = input("Enter New Course: ")

    cur.execute(
        "UPDATE student SET course = %s WHERE student_id = %s",
        (new_course, student_id)
    )

    conn.commit()

    if cur.rowcount > 0:
        print("Student Updated Successfully!")
    else:
        print("Student Not Found!")

    cur.close()
    conn.close()

def delete_student():

    conn = connect_db()
    cur = conn.cursor()

    student_id = int(input("Enter Student ID to Delete: "))

    cur.execute(
        "DELETE FROM student WHERE student_id = %s",
        (student_id,)
    )

    conn.commit()

    if cur.rowcount > 0:
        print("Student Deleted Successfully!")
    else:
        print("Student Not Found!")

    cur.close()
    conn.close()