# --- Day 2: 1202 Program Alarm ---
# --- Part Two ---
#
# "Good, the new computer seems to be working correctly! Keep it nearby during this mission - you'll probably use it
# again. Real Intcode computers support many more features than your new one, but we'll let you know what they are as
# you need them."
#
# "However, your current priority should be to complete your gravity assist around the Moon. For this mission to
# succeed, we should settle on some terminology for the parts you've already built."
#
# Intcode programs are given as a list of integers; these values are used as the initial state for the computer's
# memory. When you run an Intcode program, make sure to start by initializing memory to the program's values. A
# position in memory is called an address (for example, the first value in memory is at "address 0").
#
# Opcodes (like 1, 2, or 99) mark the beginning of an instruction. The values used immediately after an opcode,
# if any, are called the instruction's parameters. For example, in the instruction 1,2,3,4, 1 is the opcode; 2, 3,
# and 4 are the parameters. The instruction 99 contains only an opcode and has no parameters.
#
# The address of the current instruction is called the instruction pointer; it starts at 0. After an instruction
# finishes, the instruction pointer increases by the number of values in the instruction; until you add more
# instructions to the computer, this is always 4 (1 opcode + 3 parameters) for the add and multiply instructions. (
# The halt instruction would increase the instruction pointer by 1, but it halts the program instead.)
#
# "With terminology out of the way, we're ready to proceed. To complete the gravity assist, you need to determine
# what pair of inputs produces the output 19690720."
#
# The inputs should still be provided to the program by replacing the values at addresses 1 and 2, just like before.
# In this program, the value placed in address 1 is called the noun, and the value placed in address 2 is called the
# verb. Each of the two input values will be between 0 and 99, inclusive.
#
# Once the program has halted, its output is available at address 0, also just like before. Each time you try a pair
# of inputs, make sure you first reset the computer's memory to the values in the program (your puzzle input) - in
# other words, don't reuse memory from a previous attempt.
#
# Find the input noun and verb that cause the program to produce the output 19690720. What is 100 * noun + verb? (For
# example, if noun=12 and verb=2, the answer would be 1202.)

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
