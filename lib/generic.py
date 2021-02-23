import random

import numpy as np

from lib.frame_generator import generate_frame
from lib.penalty import penalty
from lib.pool_functions import random_elements
from lib.schedule_generator import generate_pool


def random_prob(prob):
    return random.choices((True, False), [prob, 1 - prob])[0]


def simple_crossover(a, b, possition=-1):
    if possition == -1:
        possition = random.randint(0, a.size)
    new_a = np.hstack((a[:possition], b[possition:]))
    new_b = np.hstack((b[:possition], a[possition:]))
    return new_a, new_b


def crossover(a, b, points=1):
    new_a = np.copy(a)
    new_b = np.copy(b)
    for i in range(points):
        new_a, new_b = simple_crossover(new_a, new_b)
    return new_a, new_b


def mutation(a, prob=0.01):
    new_a = a.copy()
    for frame_id in range(new_a.size):
        if random_prob(prob):
            new_a[frame_id] = generate_frame()
    return new_a


def ranking(pool):
    return sorted(pool, key=lambda schedule: penalty(schedule))


def next_gen(prev_gen, reproduction_number=10, surviving_number=1, crossover_points=[1, 5], mutation_prob=0.01):
    population = len(prev_gen)
    reproduction_gen = prev_gen[:reproduction_number]
    new_gen = prev_gen[:surviving_number].copy()
    while len(new_gen) < population:
        parents = random_elements(reproduction_gen, 2)
        children = crossover(*parents, random.randint(*crossover_points))
        new_gen.append(mutation(children[0], mutation_prob))
        new_gen.append(mutation(children[1], mutation_prob))
    new_gen = ranking(new_gen[:population])
    top5 = [str(penalty(sch)) for sch in new_gen[:5]]
    print("the best 5: ", ", ".join(top5))
    return new_gen


def generic_finder(time_slots, rooms, courses, groups, teachers):
    pool = generate_pool(20, time_slots, rooms, courses, groups, teachers)
    print("Start pool was created")
    i=0
    while penalty(pool[0]) != 0:
        i+=1
        print("Generation ",i)
        pool = next_gen(pool)

    return pool[0]
