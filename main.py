from lib.print_result import print_schedule
from lib.generic import generic_finder

# Generating input data
from data.data import *

print("Courses: ", courses)
print("Teachers: ", teachers)
print("Groups: ", groups)
print("Rooms:", rooms)
print("Time slots: ", time_slots)

# Run generic algorithm
schedule = generic_finder(time_slots, rooms, courses, groups, teachers)
print_schedule(schedule)