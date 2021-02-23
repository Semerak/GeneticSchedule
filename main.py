from data.data import *

# Generating input data
from lib.print_result import print_schedule
from lib.schedule_generator import generate_pool
from lib.generic import generic_finder

#courses = data_generator_courses()
print(courses)

#teachers = data_generator_teachers(courses)
print(teachers)

#groups = data_generator_groups(courses)
print(groups)

#rooms = data_generator_rooms([30,30,30,60,90,40])
print(rooms)

#time_slots = data_generator_time_slots()
print(time_slots)

# Run generic algotythm
schedule = generic_finder(time_slots, rooms, courses, groups, teachers)
print_schedule(schedule)