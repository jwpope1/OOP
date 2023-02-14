import StudentClass as S
from datetime import date


def main():
    id = input(f"Please enter your student id to begin: ")
    name = input(f"Please enter your name: ")
    dob = input(date(f"Please enter your date of birth (mm/dd/yyyy): "))
    cls = input(f"Please enter your current classification: ")

    stuid = S.Student(id, name, dob, cls)
    stuname = S.Student(id, name, dob, cls)
    studob = S.Student(id, name, dob, cls)
    stucls = S.Student(id, name, dob, cls)
