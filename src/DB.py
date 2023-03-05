import jaydebeapi as jdb
import Quaries


def connect(
    db_driver_path: str, db_url: str, db_user: str, db_password: str) -> jdb.Connection:
    """Connect to H2 database.

    Args:
        db_driver_path (str): path to database engine.
        db_url (str): url of database.
        db_user (str): username.
        db_password (str): password.

    Returns:
        jdb.Connection: connection to the database.
    """
    connection = jdb.connect('org.h2.Driver', db_url, [db_user, db_password], db_driver_path)
    return connection


def get_populations(connection: jdb.Connection) -> list[tuple]:
    """Returns all courses and their populations from database. 

    Args:
        connection (jdb.Connection): connection to the database.

    Returns:
        list[tuple]: every tuple contains name of the program and its population.
    """
    curs = connection.cursor()
    curs.execute(Quaries.quary_1)
    data: list[tuple] = curs.fetchall()
    curs.close()
    return data


def get_attendance(connection: jdb.Connection) -> list[tuple]:
    """Returns all courses and their percentages of attendance.

    Args:
        connection (jdb.Connection): connection to the database.

    Returns:
        list[tuple]: every tuple contains name of the program and 
        its percentage of attendance.
    """
    curs = connection.cursor()
    curs.execute(Quaries.quary_2)
    data: list[tuple] = curs.fetchall()
    curs.close()
    return data


def get_students(connection: jdb.Connection, program: str) -> list[tuple]:
    """Returns information about personal email, first name, last name and
    number of passed courses of every student of a particular program.

    Args:
        connection (jdb.Connection): connection to the database.
        program (str): name of the program.

    Returns:
        list[tuple]: every tuple contains student's personal email,
        first name, last name, number of all courses, number of passed 
        courses.
    """
    curs = connection.cursor()
    curs.execute(Quaries.quary_3(program))
    data: list[tuple] = curs.fetchall()
    curs.close()
    return data


def get_courses(connection: jdb.Connection, program: str) -> list[tuple]:
    """Returns all courses and number of their sessions of a particular program.

    Args:
        connection (jdb.Connection): connection to the database.
        program (str): name of the program.

    Returns:
        list[tuple]: every tuple contains name of a course and its 
        number of sessions.
    """
    curs = connection.cursor()
    curs.execute(Quaries.quary_4(program))
    data: list[tuple] = curs.fetchall()
    curs.close()
    return data


def get_course_grades(
    connection: jdb.Connection, program: str, course: str) -> list[tuple]:
    """Returns all students and their grades of a particular course.

    Args:
        connection (jdb.Connection): connection to the database.
        program (str): name of a program.
        course (str): name of a course.

    Returns:
        list[tuple]: every tuple contains student personal email,
        first name, last name, grade.
    """
    curs = connection.cursor()
    curs.execute(Quaries.quary_5(program, course))
    data: lsit[tuple] = curs.fetchall()
    curs.close()
    return data


def get_student_grades(
    connection: jdb.Connection, program: str, student: str) -> list[tuple]:
    """Returns all courses of a particular student, his grades
    and his personal email.

    Args:
        connection (jdb.Connection): _description_
        program (str): name of a program.
        student (str): first and last name of a student.

    Returns:
        list[tuple]: every tuple contains personal email, name 
        of a course and student's grade in this course.
    """
    curs = connection.cursor()
    curs.execute(Quaries.quary_6(program, student))
    data: list[tuple] = curs.fetchall()
    curs.close()
    return data