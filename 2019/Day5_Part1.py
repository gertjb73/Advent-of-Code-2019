# --- Day 5: Sunny with a Chance of Asteroids ---
# --- Part One ---
#
# You're starting to sweat as the ship makes its way toward Mercury. The Elves suggest that you get the air
# conditioner working by upgrading your ship computer to support the Thermal Environment Supervision Terminal.
#
# The Thermal Environment Supervision Terminal (TEST) starts by running a diagnostic program (your puzzle input). The
# TEST diagnostic program will run on your existing Intcode computer after a few modifications:
#
# First, you'll need to add two new instructions:
#
# Opcode 3 takes a single integer as input and saves it to the position given by its only parameter. For example,
# the instruction 3,50 would take an input value and store it at address 50.
# Opcode 4 outputs the value of its only parameter. For example, the instruction 4,50 would output the value at
# address 50.
# Programs that use these instructions will come with documentation that explains what should be connected to the
# input and output. The program 3,0,4,0,99 outputs whatever it gets as input, then halts.
#
# Second, you'll need to add support for parameter modes:
#
# Each parameter of an instruction is handled based on its parameter mode. Right now, your ship computer already
# understands parameter mode 0, position mode, which causes the parameter to be interpreted as a position - if the
# parameter is 50, its value is the value stored at address 50 in memory. Until now, all parameters have been in
# position mode.
#
# Now, your ship computer will also need to handle parameters in mode 1, immediate mode. In immediate mode,
# a parameter is interpreted as a value - if the parameter is 50, its value is simply 50.
#
# Parameter modes are stored in the same value as the instruction's opcode. The opcode is a two-digit number based
# only on the ones and tens digit of the value, that is, the opcode is the rightmost two digits of the first value in
# an instruction. Parameter modes are single digits, one per parameter, read right-to-left from the opcode: the first
# parameter's mode is in the hundreds digit, the second parameter's mode is in the thousands digit, the third
# parameter's mode is in the ten-thousands digit, and so on. Any missing modes are 0.
#
# For example, consider the program 1002,4,3,4,33.
#
# The first instruction, 1002,4,3,4, is a multiply instruction - the rightmost two digits of the first value, 02,
# indicate opcode 2, multiplication. Then, going right to left, the parameter modes are 0 (hundreds digit),
# 1 (thousands digit), and 0 (ten-thousands digit, not present and therefore zero):
#
# ABCDE
#  1002
#
# DE - two-digit opcode,      02 == opcode 2
#  C - mode of 1st parameter,  0 == position mode
#  B - mode of 2nd parameter,  1 == immediate mode
#  A - mode of 3rd parameter,  0 == position mode,
#                                   omitted due to being a leading zero
# This instruction multiplies its first two parameters. The first parameter, 4 in position mode, works like it did
# before - its value is the value stored at address 4 (33). The second parameter, 3 in immediate mode, simply has
# value 3. The result of this operation, 33 * 3 = 99, is written according to the third parameter, 4 in position
# mode, which also works like it did before - 99 is written to address 4.
#
# Parameters that an instruction writes to will never be in immediate mode.
#
# Finally, some notes:
#
# It is important to remember that the instruction pointer should increase by the number of values in the instruction
# after the instruction finishes. Because of the new instructions, this amount is no longer always 4.
# Integers can be negative: 1101,100,-1,4,0 is a valid program (find 100 + -1, store the result in position 4).
# The TEST diagnostic program will start by requesting from the user the ID of the system to test by running an input
# instruction - provide it 1, the ID for the ship's air conditioner unit.
#
# It will then perform a series of diagnostic tests confirming that various parts of the Intcode computer,
# like parameter modes, function correctly. For each test, it will run an output instruction indicating how far the
# result of the test was from the expected value, where 0 means the test was successful. Non-zero outputs mean that a
# function is not working correctly; check the instructions that were run before the output instruction to see which
# one failed.
#
# Finally, the program will output a diagnostic code and immediately halt. This final output isn't an error; an
# output followed immediately by a halt means the program finished. If all outputs were zero except the diagnostic
# code, the diagnostic program ran successfully.
#
# After providing 1 to the only input instruction and passing all the tests, what diagnostic code does the program
# produce?
#
# Puzzle input:
# 3,225,1,225,6,6,1100,1,238,225,104,0,1102,35,92,225,1101,25,55,225,1102,47,36,225,1102,17,35,225,1,165,18,224,1001,
# 224,-106,224,4,224,102,8,223,223,1001,224,3,224,1,223,224,223,1101,68,23,224,101,-91,224,224,4,224,102,8,223,223,101,
# 1,224,224,1,223,224,223,2,217,13,224,1001,224,-1890,224,4,224,102,8,223,223,1001,224,6,224,1,224,223,223,1102,69,77,
# 224,1001,224,-5313,224,4,224,1002,223,8,223,101,2,224,224,1,224,223,223,102,50,22,224,101,-1800,224,224,4,224,1002,
# 223,8,223,1001,224,5,224,1,224,223,223,1102,89,32,225,1001,26,60,224,1001,224,-95,224,4,224,102,8,223,223,101,2,224,
# 224,1,223,224,223,1102,51,79,225,1102,65,30,225,1002,170,86,224,101,-2580,224,224,4,224,102,8,223,223,1001,224,6,224,
# 1,223,224,223,101,39,139,224,1001,224,-128,224,4,224,102,8,223,223,101,3,224,224,1,223,224,223,1102,54,93,225,4,223,
# 99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,
# 227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,
# 294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1008,677,677,224,
# 1002,223,2,223,1005,224,329,101,1,223,223,7,677,677,224,102,2,223,223,1006,224,344,101,1,223,223,108,677,677,224,1002,
# 223,2,223,1006,224,359,1001,223,1,223,7,677,226,224,1002,223,2,223,1005,224,374,1001,223,1,223,1107,677,226,224,1002,
# 223,2,223,1005,224,389,1001,223,1,223,107,226,677,224,102,2,223,223,1005,224,404,1001,223,1,223,1108,226,677,224,1002,
# 223,2,223,1006,224,419,101,1,223,223,107,226,226,224,102,2,223,223,1005,224,434,1001,223,1,223,108,677,226,224,1002,
# 223,2,223,1006,224,449,101,1,223,223,108,226,226,224,102,2,223,223,1006,224,464,1001,223,1,223,1007,226,226,224,1002,
# 223,2,223,1005,224,479,101,1,223,223,8,677,226,224,1002,223,2,223,1006,224,494,101,1,223,223,1007,226,677,224,102,2,
# 223,223,1006,224,509,101,1,223,223,7,226,677,224,1002,223,2,223,1005,224,524,101,1,223,223,107,677,677,224,102,2,223,
# 223,1005,224,539,101,1,223,223,1008,677,226,224,1002,223,2,223,1005,224,554,1001,223,1,223,1008,226,226,224,1002,223,
# 2,223,1006,224,569,1001,223,1,223,1108,226,226,224,102,2,223,223,1005,224,584,101,1,223,223,1107,226,677,224,1002,223,
# 2,223,1005,224,599,1001,223,1,223,8,226,677,224,1002,223,2,223,1006,224,614,1001,223,1,223,1108,677,226,224,102,2,223,
# 223,1005,224,629,1001,223,1,223,8,226,226,224,1002,223,2,223,1005,224,644,1001,223,1,223,1107,677,677,224,1002,223,2,
# 223,1005,224,659,1001,223,1,223,1007,677,677,224,1002,223,2,223,1005,224,674,101,1,223,223,4,223,99,226


initial_program = [3, 225, 1, 225, 6, 6, 1100, 1, 238, 225, 104, 0, 1102, 35, 92, 225, 1101, 25, 55, 225, 1102, 47, 36,
                   225, 1102, 17, 35, 225, 1, 165, 18, 224, 1001, 224, -106, 224, 4, 224, 102, 8, 223, 223, 1001, 224,
                   3, 224, 1, 223, 224, 223, 1101, 68, 23, 224, 101, -91, 224, 224, 4, 224, 102, 8, 223, 223, 101, 1,
                   224, 224, 1, 223, 224, 223, 2, 217, 13, 224, 1001, 224, -1890, 224, 4, 224, 102, 8, 223, 223, 1001,
                   224, 6, 224, 1, 224, 223, 223, 1102, 69, 77, 224, 1001, 224, -5313, 224, 4, 224, 1002, 223, 8, 223,
                   101, 2, 224, 224, 1, 224, 223, 223, 102, 50, 22, 224, 101, -1800, 224, 224, 4, 224, 1002, 223, 8,
                   223, 1001, 224, 5, 224, 1, 224, 223, 223, 1102, 89, 32, 225, 1001, 26, 60, 224, 1001, 224, -95, 224,
                   4, 224, 102, 8, 223, 223, 101, 2, 224, 224, 1, 223, 224, 223, 1102, 51, 79, 225, 1102, 65, 30, 225,
                   1002, 170, 86, 224, 101, -2580, 224, 224, 4, 224, 102, 8, 223, 223, 1001, 224, 6, 224, 1, 223, 224,
                   223, 101, 39, 139, 224, 1001, 224, -128, 224, 4, 224, 102, 8, 223, 223, 101, 3, 224, 224, 1, 223,
                   224, 223, 1102, 54, 93, 225, 4, 223, 99, 0, 0, 0, 677, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1105, 0,
                   99999, 1105, 227, 247, 1105, 1, 99999, 1005, 227, 99999, 1005, 0, 256, 1105, 1, 99999, 1106, 227,
                   99999, 1106, 0, 265, 1105, 1, 99999, 1006, 0, 99999, 1006, 227, 274, 1105, 1, 99999, 1105, 1, 280,
                   1105, 1, 99999, 1, 225, 225, 225, 1101, 294, 0, 0, 105, 1, 0, 1105, 1, 99999, 1106, 0, 300, 1105, 1,
                   99999, 1, 225, 225, 225, 1101, 314, 0, 0, 106, 0, 0, 1105, 1, 99999, 1008, 677, 677, 224, 1002, 223,
                   2, 223, 1005, 224, 329, 101, 1, 223, 223, 7, 677, 677, 224, 102, 2, 223, 223, 1006, 224, 344, 101, 1,
                   223, 223, 108, 677, 677, 224, 1002, 223, 2, 223, 1006, 224, 359, 1001, 223, 1, 223, 7, 677, 226, 224,
                   1002, 223, 2, 223, 1005, 224, 374, 1001, 223, 1, 223, 1107, 677, 226, 224, 1002, 223, 2, 223, 1005,
                   224, 389, 1001, 223, 1, 223, 107, 226, 677, 224, 102, 2, 223, 223, 1005, 224, 404, 1001, 223, 1, 223,
                   1108, 226, 677, 224, 1002, 223, 2, 223, 1006, 224, 419, 101, 1, 223, 223, 107, 226, 226, 224, 102, 2,
                   223, 223, 1005, 224, 434, 1001, 223, 1, 223, 108, 677, 226, 224, 1002, 223, 2, 223, 1006, 224, 449,
                   101, 1, 223, 223, 108, 226, 226, 224, 102, 2, 223, 223, 1006, 224, 464, 1001, 223, 1, 223, 1007, 226,
                   226, 224, 1002, 223, 2, 223, 1005, 224, 479, 101, 1, 223, 223, 8, 677, 226, 224, 1002, 223, 2, 223,
                   1006, 224, 494, 101, 1, 223, 223, 1007, 226, 677, 224, 102, 2, 223, 223, 1006, 224, 509, 101, 1, 223,
                   223, 7, 226, 677, 224, 1002, 223, 2, 223, 1005, 224, 524, 101, 1, 223, 223, 107, 677, 677, 224, 102,
                   2, 223, 223, 1005, 224, 539, 101, 1, 223, 223, 1008, 677, 226, 224, 1002, 223, 2, 223, 1005, 224,
                   554, 1001, 223, 1, 223, 1008, 226, 226, 224, 1002, 223, 2, 223, 1006, 224, 569, 1001, 223, 1, 223,
                   1108, 226, 226, 224, 102, 2, 223, 223, 1005, 224, 584, 101, 1, 223, 223, 1107, 226, 677, 224, 1002,
                   223, 2, 223, 1005, 224, 599, 1001, 223, 1, 223, 8, 226, 677, 224, 1002, 223, 2, 223, 1006, 224, 614,
                   1001, 223, 1, 223, 1108, 677, 226, 224, 102, 2, 223, 223, 1005, 224, 629, 1001, 223, 1, 223, 8, 226,
                   226, 224, 1002, 223, 2, 223, 1005, 224, 644, 1001, 223, 1, 223, 1107, 677, 677, 224, 1002, 223, 2,
                   223, 1005, 224, 659, 1001, 223, 1, 223, 1007, 677, 677, 224, 1002, 223, 2, 223, 1005, 224, 674, 101,
                   1, 223, 223, 4, 223, 99, 226]

# initial_program = [1101, 100, -1, 4, 0]
# initial_program = [3, 0, 4, 0, 99]

param1_mode_pos = 2
param2_mode_pos = 1
param3_mode_pos = 0


def determine_opcode_and_process(opcode, pointer, end_reached):
    # print("Determine Opcode and Process")

    # ABCDE
    #  1002
    # DE - two-digit opcode,      02 == opcode 2
    #  C - mode of 1st parameter,  0 == position mode
    #  B - mode of 2nd parameter,  1 == immediate mode
    #  A - mode of 3rd parameter,  0 == position mode,
    #                                   omitted due to being a leading zero
    # parameter mode 0 = position mode, which causes the parameter to be interpreted as a position.
    # parameter mode 1 = immediate mode. the parameter is interpreted as a value

    total_opcode_length = 5

    total_opcode = str(opcode).zfill(total_opcode_length)
    real_opcode = int(total_opcode[total_opcode_length - 2]) * 10 + int(total_opcode[total_opcode_length - 1])

    if real_opcode == 1:
        pointer = process_opcode1(real_opcode, total_opcode, pointer)
    if real_opcode == 2:
        pointer = process_opcode2(real_opcode, total_opcode, pointer)
    if real_opcode == 3:
        pointer = process_opcode3(real_opcode, total_opcode, pointer)
    if real_opcode == 4:
        pointer = process_opcode4(real_opcode, total_opcode, pointer)

    if real_opcode == 99:
        end_reached = process_opcode99(real_opcode, total_opcode, pointer, end_reached)

    return pointer, end_reached


def get_mode_value(parameter_mode, parameter):
    if parameter_mode == 0:  # Position mode
        # print("Param 1 Mode: Position, ", end='')
        return program[parameter]
    if parameter_mode == 1:  # Immediate mode
        # print("Param 1 Mode: Immediate, ", end='')
        return parameter


def process_opcode1(processed_opcode, filled_opcode, pointer):
    print("Process Opcode 1 ==>", end=' ')
    param1 = program[pointer + 1]
    param2 = program[pointer + 2]
    param3 = program[pointer + 3]

    # parameter mode 0 = position mode, which causes the parameter to be interpreted as a position.
    # parameter mode 1 = immediate mode. the parameter is interpreted as a value
    param1_mode = int(filled_opcode[param1_mode_pos])
    param2_mode = int(filled_opcode[param2_mode_pos])
    param3_mode = int(filled_opcode[param3_mode_pos])

    print("Filled Opcode:", filled_opcode, end=' ')
    print("Processed Opcode:", processed_opcode, end=' ')
    print("Param1:", param1, "Mode:", param1_mode, end=' ')
    print("Param2:", param2, "Mode:", param2_mode, end=' ')
    print("Param3:", param3, "Mode:", param3_mode)

    value1 = get_mode_value(param1_mode, param1)
    value2 = get_mode_value(param2_mode, param2)
    value3 = param3

    program[value3] = value1 + value2

    return pointer + 4


def process_opcode2(processed_opcode, filled_opcode, pointer):
    print("Process Opcode 2 ==>", end=' ')
    param1 = program[pointer + 1]
    param2 = program[pointer + 2]
    param3 = program[pointer + 3]

    # parameter mode 0 = position mode, which causes the parameter to be interpreted as a position.
    # parameter mode 1 = immediate mode. the parameter is interpreted as a value
    param1_mode = int(filled_opcode[param1_mode_pos])
    param2_mode = int(filled_opcode[param2_mode_pos])
    param3_mode = int(filled_opcode[param3_mode_pos])

    print("Filled Opcode:", filled_opcode, end=' ')
    print("Processed Opcode:", processed_opcode, end=' ')
    print("Param1:", param1, "Mode:", param1_mode, end=' ')
    print("Param2:", param2, "Mode:", param2_mode, end=' ')
    print("Param3:", param3, "Mode:", param3_mode)

    value1 = get_mode_value(param1_mode, param1)
    value2 = get_mode_value(param2_mode, param2)
    value3 = param3

    program[value3] = value1 * value2

    return pointer + 4


def process_opcode3(processed_opcode, filled_opcode, pointer):
    # Opcode 3 takes a single integer as input and saves it to the position given by its only parameter. For example,
    # the instruction 3,50 would take an input value and store it at address 50.
    print("Process Opcode 3 ==>", end=' ')
    param1 = program[pointer + 1]

    # parameter mode 0 = position mode, which causes the parameter to be interpreted as a position.
    # parameter mode 1 = immediate mode. the parameter is interpreted as a value
    param1_mode = int(filled_opcode[param1_mode_pos])

    print("Filled Opcode:", filled_opcode, end=' ')
    print("Processed Opcode:", processed_opcode, end=' ')
    print("Param1:", param1, "Mode:", param1_mode)

    number_input_opcode_3 = input("Enter number : ")
    program[param1] = int(number_input_opcode_3)

    return pointer + 2


def process_opcode4(processed_opcode, filled_opcode, pointer):
    # Opcode 4 outputs the value of its only parameter. For example, the instruction 4,50 would output the value at
    # address 50.
    print("Process Opcode 4 ==>", end=' ')
    param1 = program[pointer + 1]

    # parameter mode 0 = position mode, which causes the parameter to be interpreted as a position.
    # parameter mode 1 = immediate mode. the parameter is interpreted as a value
    param1_mode = int(filled_opcode[param1_mode_pos])

    print("Filled Opcode:", filled_opcode, end=' ')
    print("Processed Opcode:", processed_opcode, end=' ')
    print("Param1:", param1, "Mode:", param1_mode)

    # value1 = get_mode_value(param1_mode, param1)
    value1 = program[param1]
    print("Opcode: 4, Param:", param1, ", Value:", value1)

    return pointer + 2


def process_opcode99(processed_opcode, filled_opcode, pointer, end):
    print("Process Opcode 99 ==>", end=' ')

    print("Filled Opcode:", filled_opcode, end=' ')
    print("Processed Opcode:", processed_opcode)

    end = True
    return end


program = initial_program.copy()
print("\nInitial program:", *program, "\n")
noun = verb = 0
max_noun = max_verb = 99
pos0 = 0
end_of_program = False

while not end_of_program:
    (pos0, end_of_program) = determine_opcode_and_process(program[pos0], pos0, end_of_program)
    # print("Current program:", *program)

print("Final program  :", *program)
