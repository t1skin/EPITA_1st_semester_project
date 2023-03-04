import jaydebeapi as jdb
import Quaries


def connect(
    db_driver_path: str, db_url: str, db_user: str, db_password: str) -> jdb.Connection:

    connection = jdb.connect('org.h2.Driver', db_url, [db_user, db_password], db_driver_path)
    return connection


def get_populations(connection: jdb.Connection) -> list[tuple]:

    curs = connection.cursor()
    curs.execute(Quaries.quary_1)
    data: list[tuple] = curs.fetchall()
    curs.close()
    return data


def get_attendance(connection: jdb.Connection) -> list[tuple]:

    curs = connection.cursor()
    curs.execute(Quaries.quary_2)
    data: list[tuple] = curs.fetchall()
    curs.close()
    return data


def get_students(connection: jdb.Connection, program: str) -> list[tuple]:

    curs = connection.cursor()
    curs.execute(Quaries.quary_3(program))
    data: list[tuple] = curs.fetchall()
    curs.close()
    return data


def get_courses(connection: jdb.Connection, program: str) -> list[tuple]:
    
    curs = connection.cursor()
    curs.execute(Quaries.quary_4(program))
    data: list[tuple] = curs.fetchall()
    curs.close()
    return data


def get_course_grades(
    connection: jdb.Connection, program: str, course: str) -> list[tuple]:
    
    curs = connection.cursor()
    curs.execute(Quaries.quary_5(program, course))
    data: lsit[tuple] = curs.fetchall()
    curs.close()
    return data


def get_student_grades(
    connection: jdb.Connection, program: str, student: str) -> list[tuple]:

    curs = connection.cursor()
    curs.execute(Quaries.quary_6(program, student))
    data: list[tuple] = curs.fetchall()
    curs.close()
    return data