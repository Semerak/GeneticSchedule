import numpy as np

from lib.frame_generator import generate_frame
from data.data import *


def generate_schedule(time_slots, rooms, courses, groups, teachers):
    schedule = np.zeros_like(time_slots, dtype=object)
    for i in range(len(time_slots)):
        schedule[i] = generate_frame(rooms, courses, groups, teachers)
    return schedule


def generate_pool(quantity, time_slots, rooms, courses, groups, teachers):
    pool = [generate_schedule(time_slots, rooms, courses, groups, teachers) for i in range(quantity)]
    return pool
