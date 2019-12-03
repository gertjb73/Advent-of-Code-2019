# --- Day 1: The Tyranny of the Rocket Equation ---
# --- Part One ---
#
# Santa has become stranded at the edge of the Solar System while delivering presents to other planets! To accurately
# calculate his position in space, safely align his warp drive, and return to Earth in time to save Christmas,
# he needs you to bring him measurements from fifty stars.
#
# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second
# puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!
#
# The Elves quickly load you into a spacecraft and prepare to launch.
#
# At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper. They haven't determined the amount of
# fuel required yet.
#
# Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module,
# take its mass, divide by three, round down, and subtract 2.
#
# For example:
#
# For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
# For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
# For a mass of 1969, the fuel required is 654.
# For a mass of 100756, the fuel required is 33583.
# The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually calculate the fuel needed
# for the mass of each module (your puzzle input), then add together all the fuel values.
#
# What is the sum of the fuel requirements for all of the modules on your spacecraft?

module_mass = [70904, 66770, 118678, 58460, 128566, 60820, 107153, 113196, 52413, 118335, 96711, 88120, 129744, 64049,
               90586, 54466, 55693, 102407, 148273, 110281, 111814, 60951, 102879, 135253, 130081, 86645, 72934, 147097,
               74578, 124073, 100003, 103314, 86468, 84557, 94232, 120012, 64372, 143081, 96664, 148076, 147357, 139897,
               113139, 143022, 144298, 81293, 53679, 139311, 107156, 121730, 132519, 132666, 80464, 111118, 76734,
               139023, 111287, 126811, 130539, 129173, 67549, 102058, 72673, 91194, 64753, 59488, 126300, 94407, 126813,
               60028, 95129, 79270, 123465, 60966, 111920, 76549, 110195, 119975, 112557, 129676, 104941, 89583, 121895,
               108901, 135247, 75129, 148646, 131128, 78931, 111637, 72752, 140761, 57387, 85684, 77596, 134159, 63031,
               148361, 133856, 82022]

total_fuel_needed = 0

for mass in module_mass:
    fuel_needed = (mass // 3) - 2 if ((mass // 3) -2) > 0 else 0
    total_fuel_needed += fuel_needed

print("Result for Advent of Code", total_fuel_needed)
