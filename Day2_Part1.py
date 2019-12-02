program = [
    1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 6, 1, 19, 1, 19, 5, 23, 2, 10, 23, 27, 2, 27, 13, 31, 1, 10, 31,
    35, 1, 35, 9, 39, 2, 39, 13, 43, 1, 43, 5, 47, 1, 47, 6, 51, 2, 6, 51, 55, 1, 5, 55, 59, 2, 9, 59, 63, 2, 6, 63,
    67, 1, 13, 67, 71, 1, 9, 71, 75, 2, 13, 75, 79, 1, 79, 10, 83, 2, 83, 9, 87, 1, 5, 87, 91, 2, 91, 6, 95, 2, 13, 95,
    99, 1, 99, 5, 103, 1, 103, 2, 107, 1, 107, 10, 0, 99, 2, 0, 14, 0]

program[1] = 12
program[2] = 2

print("\nInitial program:", *program)

pos0 = 0
end_of_program = False
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
    # print("Current program:\t", *program)

print("Final program  :", *program)
print("Result for Advent of Code: ", program[0])
