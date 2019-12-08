# --- Day 5: Sunny with a Chance of Asteroids ---
# --- Part Two ---
#
# The air conditioner comes online! Its cold air feels good for a while, but then the TEST alarms start to go off.
# Since the air conditioner can't vent its heat anywhere but back into the spacecraft, it's actually making the air
# inside the ship warmer.
#
# Instead, you'll need to use the TEST to extend the thermal radiators. Fortunately, the diagnostic program (your
# puzzle input) is already equipped for this. Unfortunately, your Intcode computer is not.
#
# Your computer is only missing a few opcodes:
# - Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the
#   second parameter. Otherwise, it does nothing.
# - Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the
#   second parameter. Otherwise, it does nothing.
# - Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given
#   by the third parameter. Otherwise, it stores 0.
# - Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by
#   the third parameter. Otherwise, it stores 0.
# Like all instructions, these instructions need to support parameter modes as described above.
#
# Normally, after an instruction is finished, the instruction pointer increases by the number of values in that
# instruction. However, if the instruction modifies the instruction pointer, that value is used and the instruction
# pointer is not automatically increased.
#
# For example, here are several programs that take one input, compare it to the value 8, and then produce one output:
# - 3,9,8,9,10,9,4,9,99,-1,8 - Using position mode, consider whether the input is equal to 8; output 1 (if it is) or 0
#   (if it is not).
# - 3,9,7,9,10,9,4,9,99,-1,8 - Using position mode, consider whether the input is less than 8; output 1 (if it is) or 0
#   (if it is not).
# - 3,3,1108,-1,8,3,4,3,99 - Using immediate mode, consider whether the input is equal to 8; output 1 (if it is) or 0
#   (if it is not).
# - 3,3,1107,-1,8,3,4,3,99 - Using immediate mode, consider whether the input is less than 8; output 1 (if it is) or 0
#   (if it is not).
#
# Here are some jump tests that take an input, then output 0 if the input was zero or 1 if the input was non-zero:
# - 3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9 (using position mode)
# - 3,3,1105,-1,9,1101,0,0,12,4,12,99,1 (using immediate mode)
#
# Here's a larger example:
# - 3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
#   1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
#   999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99
#
# The above example program uses an input instruction to ask for a single number. The program will then output 999 if
# the input value is below 8, output 1000 if the input value is equal to 8, or output 1001 if the input value is
# greater than 8.
#
# This time, when the TEST diagnostic program runs its input instruction to get the ID of the system to test,
# provide it 5, the ID for the ship's thermal radiator controller. This diagnostic test suite only outputs one
# number, the diagnostic code.
#
# What is the diagnostic code for system ID 5?
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
