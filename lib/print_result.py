from data.data import *


def print_frame(frame, time_id):
    time = time_slots[time_id]
    w = time['week']
    d = time['day']
    t = time['time']
    print(f"Week {w}, {d}, time: {t}")
    for room_id in range(len(frame)):
        if frame[room_id][1] == -1:
            print(f"\tRoom {room_id} Empty")
        else:
            groups_st = ", ".join([groups[g]['name'] for g in frame[room_id][0]])
            te = teachers[frame[room_id][1]]['name']
            c = courses[frame[room_id][2]]['name']
            ct = courses[frame[room_id][2]]['type']
            print(f"\tRoom {room_id}, group: {groups_st}, teacher: {te}, course: {c} ({ct})")


def print_schedule(schedule):
    for i in range(len(schedule)):
        print_frame(schedule[i], i)
        print("\n")
