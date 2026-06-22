from flask import Flask, render_template,request,redirect, url_for
from db import connect_db 
import psycopg2

app = Flask(__name__)

@app.route("/")
def home():

    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM student")

    total_students = cur.fetchone()[0]

    cur.close()
    conn.close()

    return render_template(
        "index.html",
        total_students=total_students
    )

@app.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "POST":

        name = request.form["name"]
        age = request.form["age"]
        gender = request.form["gender"]
        email = request.form["email"]
        phone = request.form["phone"]
        course = request.form["course"]

        conn = connect_db()
        cur = conn.cursor()

        cur.execute(
            """
            INSERT INTO student
            (name, age, gender, email, phone_no, course)
            VALUES (%s,%s,%s,%s,%s,%s)
            """,
            (name, age, gender, email, phone, course)
        )

        conn.commit()

        cur.close()
        conn.close()

        return redirect(url_for("view"))

    return render_template("add_student.html")

@app.route("/search", methods=["GET", "POST"])
def search():

    students = []

    if request.method == "POST":

        name = request.form["name"]

        conn = connect_db()
        cur = conn.cursor()

        query = """
        SELECT * FROM student
        WHERE name ILIKE %s
        """

        cur.execute(query, ('%' + name + '%',))

        students = cur.fetchall()

        cur.close()
        conn.close()

    return render_template(
        "search_student.html",
        students=students
    )
@app.route("/view")
def view():

    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM student")

    students = cur.fetchall()

    cur.close()
    conn.close()

    return render_template(
        "view_students.html",
        students=students
    )

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):

    conn = connect_db()
    cur = conn.cursor()

    if request.method == "POST":

        name = request.form["name"]
        age = request.form["age"]
        gender = request.form["gender"]
        email = request.form["email"]
        phone = request.form["phone"]
        course = request.form["course"]

        cur.execute("""
        UPDATE student
        SET
        name=%s,
        age=%s,
        gender=%s,
        email=%s,
        phone_no=%s,
        course=%s
        WHERE student_id=%s
        """,
        (name, age, gender, email, phone, course, id))

        conn.commit()

        cur.close()
        conn.close()

        return redirect(url_for("view"))

    cur.execute(
        "SELECT * FROM student WHERE student_id=%s",
        (id,)
    )

    student = cur.fetchone()

    cur.close()
    conn.close()

    return render_template(
        "edit_student.html",
        student=student
    )
@app.route("/delete/<int:id>")
def delete(id):

    conn = connect_db()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM student WHERE student_id=%s",
        (id,)
    )

    conn.commit()

    cur.close()
    conn.close()

    return redirect(url_for("view"))

if __name__ == "__main__":
    app.run(debug=True)