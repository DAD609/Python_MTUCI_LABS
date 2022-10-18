from tkinter import N


groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "group": ["БАП1801"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "group": ["БСТ1702"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "group": ["БВТ1702"],
        "marks": [5, 5, 5]
    }
]
# for student in students:
#     mer = str(student["marks"])/
def ocenka(rate, students):
    for student in students:
        marks = student["marks"]
        midval = 0
        for i in marks:
            midval += i
        midval/=len(marks)
        if midval>rate:
            print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
        
            print(student["name"].ljust(15), student["surname"].ljust(10), str(student["group"]).ljust(30), str(student["marks"]).ljust(20))



grade = input('Введите среднюю оценку ')

ocenka(float(grade), groupmates)

