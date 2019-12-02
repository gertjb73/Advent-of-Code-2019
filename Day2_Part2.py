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
