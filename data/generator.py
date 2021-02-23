import random

from lib.pool_functions import random_elements


# Generates input data

def data_generator_courses():
    names = ["Math Analysis", "Programming", "Data Base", "Math Logic", "Algorithms", "Crypto", "Linguistics",
             "Cloud systems"]
    types = ["lecture", "practice"]
    hours_range = [10, 20]

    courses = []
    i = -1
    for name in names:
        for t in types:
            i += 1
            course = {
                "id": i,
                "name": name,
                "type": t,
                "hours": random.randint(*hours_range)
            }
            courses.append(course)
    return courses


def data_generator_teachers(courses):
    names = ["Green", "Brown", "Wood", "Steal", "Water", "Fire"]
    density = [1, 3]
    teachers = []
    for i in range(len(names)):
        teachers.append({
            "id": i,
            "name": names[i],
            "courses": []
        })
    teachers_len = len(teachers)
    for c_id in range(len(courses)):
        dens = random.randint(*density)
        teach = random_elements(range(teachers_len), dens)
        for t in teach:
            teachers[t]['courses'].append(c_id)
    return teachers


def data_generator_groups(courses):
    names = ["K-10", "K-11", "K-12", "K-20", "K-21", "K-22"]
    students_range = [25, 35]
    courses_quantity = [5, 7]
    groups = []
    courses_len = len(courses)
    n_id = -1
    for name in names:
        n_id += 1
        groups.append({
            "id": n_id,
            "name": name,
            "students": random.randint(*students_range),
            "courses": random_elements(range(courses_len), random.randint(*courses_quantity))
        })
    return groups


def data_generator_rooms(init=[]):
    rooms = []
    if init:
        for r_id in range(len(init)):
            rooms.append({
                "id": r_id,
                "size": init[r_id]
            })
    else:
        n = 6
        size_range = [30, 90]
        for r_id in range(n):
            rooms.append({
                "id": r_id,
                "size": random.randint(*size_range)
            })
    return rooms


def data_generator_time_slots():
    weeks = range(12)
    days = ["Mon", "Tue", "Wen", "Thu", "Fri"]
    slots = ["8:40 - 10:15", "10:35 - 12:10", "12:20 - 13:55"]
    time_slots = []
    i = -1
    for week in weeks:
        for day in days:
            for time in slots:
                i += 1
                time_slots.append({
                    'id': i,
                    'week': week + 1,
                    'day': day,
                    'time': time
                })

    return time_slots
