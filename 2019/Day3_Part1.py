# --- Day 3: Crossed Wires ---
# --- Part Two ---
#
# The gravity assist was successful, and you're well on your way to the Venus refuelling station. During the rush
# back on Earth, the fuel management system wasn't completely installed, so that's next on the priority list.
#
# Opening the front panel reveals a jumble of wires. Specifically, two wires are connected to a central port and
# extend outward on a grid. You trace the path each wire takes as it leaves the central port, one wire per line of
# text (your puzzle input).
#
# The wires twist and turn, but the two wires occasionally cross paths. To fix the circuit, you need to find the
# intersection point closest to the central port. Because the wires are on a grid, use the Manhattan distance for
# this measurement. While the wires do technically cross right at the central port where they both start, this point
# does not count, nor does a wire count as crossing with itself.
#
# For example, if the first wire's path is R8,U5,L5,D3, then starting from the central port (o), it goes right 8,
# up 5, left 5, and finally down 3:
#
# ...........
# ...........
# ...........
# ....+----+.
# ....|....|.
# ....|....|.
# ....|....|.
# .........|.
# .o-------+.
# ...........
# Then, if the second wire's path is U7,R6,D4,L4, it goes up 7, right 6, down 4, and left 4:
#
# ...........
# .+-----+...
# .|.....|...
# .|..+--X-+.
# .|..|..|.|.
# .|.-X--+.|.
# .|..|....|.
# .|.......|.
# .o-------+.
# ...........
#
# These wires cross at two locations (marked X), but the lower-left one is closer to the central port: its distance
# is 3 + 3 = 6.
#
# Here are a few more examples:
#
# R75,D30,R83,U83,L12,D49,R71,U7,L72
# U62,R66,U55,R34,D71,R55,D58,R83 = distance 159
# R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
# U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = distance 135
# What is the Manhattan distance from the central port to the closest intersection?

initial_program = [
    1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 6, 1, 19, 1, 19, 5, 23, 2, 10, 23, 27, 2, 27, 13, 31, 1, 10, 31,
    35, 1, 35, 9, 39, 2, 39, 13, 43, 1, 43, 5, 47, 1, 47, 6, 51, 2, 6, 51, 55, 1, 5, 55, 59, 2, 9, 59, 63, 2, 6, 63,
    67, 1, 13, 67, 71, 1, 9, 71, 75, 2, 13, 75, 79, 1, 79, 10, 83, 2, 83, 9, 87, 1, 5, 87, 91, 2, 91, 6, 95, 2, 13, 95,
    99, 1, 99, 5, 103, 1, 103, 2, 107, 1, 107, 10, 0, 99, 2, 0, 14, 0]

program = initial_program.copy()

print("\nInitial program:", *program)

needed_result = 19690720
noun = verb = 0
max_noun = max_verb = 99
pos0 = 0
end_of_program = False
result_found = False

program[1] = noun
program[2] = verb

while noun <= max_noun and not result_found: # and not end_of_program:
    verb = 0

    while verb <= max_verb and not result_found: # and not end_of_program:
        program = initial_program.copy()
        program[1] = noun
        program[2] = verb
        pos0 = 0
        end_of_program = False
        # print("Current program:", *program)
        while not end_of_program:
            pos1 = pos0 + 1
            pos2 = pos0 + 2
            pos3 = pos0 + 3

            key_pos0 = program[pos0]
            key_pos1 = program[pos1]
            key_pos2 = program[pos2]
            key_pos3 = program[pos3]

            value_pos0 = program[key_pos0]
            value_pos1 = program[key_pos1]
            value_pos2 = program[key_pos2]
            value_pos3 = program[key_pos3]

            # print("Pos", pos0, pos1, pos2, pos3, end=' ')
            # print("Key", key_pos0, key_pos1, key_pos2, key_pos3, end=' ')
            # print("Value", value_pos0, value_pos1, value_pos2, value_pos3, end=' ')

            if key_pos0 == 1:
                result = value_pos1 + value_pos2
                program[key_pos3] = result
                # print("Result", value_pos1, "+", value_pos2, "=", result, ":", program[key_pos3])
                pos0 += 4
            if key_pos0 == 2:
                result = value_pos1 * value_pos2
                program[key_pos3] = result
                # print("Result", value_pos1, "*", value_pos2, "=", result, ":", program[key_pos3])
                pos0 += 4
            if key_pos0 == 99:
                pos0 += 1
                end_of_program = True
            # print("Noun:", noun, "Verb:", verb, "Current program:", *program)

        if program[0] == needed_result:
            # print("Noun:", noun, "Verb:", verb, "Result:", program[0])
            print("Current program:", *program)
            aoc_result = (100 * noun) + verb
            result_found = True
        verb += 1
    noun += 1

print("Final program  :", *program)
print("Result for Advent of Code: ", aoc_result)
