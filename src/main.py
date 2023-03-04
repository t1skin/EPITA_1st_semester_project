from flask import Flask, render_template
import DB


path_to_h2_jar: str = 'C:/Users/trofi/H2/bin/h2-2.1.214.jar'
url: str = 'jdbc:h2:tcp://localhost/./data_for_project'
user: str = 'tiskin'
password: str = 'epita'


connection: DB.jdb.Connection = DB.connect(path_to_h2_jar, url, user, password)


app = Flask(__name__)


@app.route('/')
def index():
    attendance = DB.get_attendance(connection)
    populations = DB.get_populations(connection)
    return render_template('index.html', populations=populations, attendance=attendance)


@app.route('/population/<string:program>')
def population_page(program):
    courses = DB.get_courses(connection, program)
    students = DB.get_students(connection, program)
    return render_template('population.html', program=program, courses=courses, students=students)


@app.route('/<string:program>/grades/<string:course>')
def course_grades_page(program, course):
    grades = DB.get_course_grades(connection, program, course)
    return render_template('grades.html', program=program, course=course, grades=grades)


@app.route('/<string:program>/<string:student>')
def student_grades_page(program, student):
    student = student.replace('_', ' ')
    grades = DB.get_student_grades(connection, program, student)
    return render_template('student.html', program=program, student=student, grades=grades)


if __name__ == '__main__':
    app.run(debug=True)