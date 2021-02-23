import random

import numpy as np

from lib.pool_functions import random_elements
from data.data import *


def check_lesson(room, groups, teacher, course, print_flag=False):
    if print_flag:
        print(room, "\n", groups, "\n", teacher, "\n", course)
    if course['id'] not in teacher['courses']:
        if print_flag:
            print("teacher courses")
        return False
    people = 0
    for g in groups:
        people += g['students']
        if course['id'] not in g['courses']:
            if print_flag:
                print("group courses")
            return False
    if room['size'] < people:
        return False

    return True


def check_teacher(teacher, course):
    if course['id'] not in teacher['courses']:
        return False
    return True


def create_group(room_size, groups, course):
    good_groups = []
    groups_copy = random_elements(groups)
    for g_id in range(len(groups_copy)):
        if course['id'] in groups_copy[g_id]['courses']:
            if room_size >= groups_copy[g_id]['students']:
                group = groups_copy.pop(g_id)
                good_groups.append(group)
                next_div = create_group(room_size - group['students'], groups_copy, course)
                good_groups.extend(next_div[0])
                rest_groups = next_div[1]
                return [good_groups, rest_groups]

    return [good_groups, groups_copy]


def random_element_index(pool):
    element_i = random.randint(-1, len(pool) - 1)
    return element_i


def generate_frame(rooms=rooms, courses=courses, groups=groups, teachers=teachers):
    frame = np.zeros((len(rooms), 3), dtype=object)

    free_teachers = random_elements(teachers)

    free_groups = random_elements(groups)

    for room_id in range(len(rooms)):
        done = False
        while not done:
            course_id = random_element_index(courses)
            if course_id == -1:
                frame[room_id] = np.array([-1, -1, -1])
                done = True
            else:

                course = courses[course_id]
                # find teacher
                teachers_iter = iter(range(len(free_teachers)))

                good_teacher = False
                teacher_id = 0
                while not good_teacher and teacher_id is not None:
                    teacher_id = next(teachers_iter, None)
                    if teacher_id is not None:
                        good_teacher = check_teacher(free_teachers[teacher_id], course)
                if teacher_id is not None:

                    # create group
                    good_groups, free_groups = create_group(rooms[room_id]['size'], free_groups, course)

                    if good_groups:
                        np_groups = np.array([g['id'] for g in good_groups])
                        frame[room_id] = np.array([np_groups, free_teachers[teacher_id]['id'], course['id']],
                                                  dtype=object)
                        done = True
                        free_teachers.pop(teacher_id)

    return frame
