# --- Day 1: The Tyranny of the Rocket Equation ---
# --- Part Two ---
#
# During the second Go / No Go poll, the Elf in charge of the Rocket Equation Double-Checker stops the launch
# sequence. Apparently, you forgot to include additional fuel for the fuel you just added.
#
# Fuel itself requires fuel just like a module - take its mass, divide by three, round down, and subtract 2. However,
# that fuel also requires fuel, and that fuel requires fuel, and so on. Any mass that would require negative fuel
# should instead be treated as if it requires zero fuel; the remaining mass, if any, is instead handled by wishing
# really hard, which has no mass and is outside the scope of this calculation.
#
# So, for each module mass, calculate its fuel and add it to the total. Then, treat the fuel amount you just
# calculated as the input mass and repeat the process, continuing until a fuel requirement is zero or negative. For
# example:
#
# A module of mass 14 requires 2 fuel. This fuel requires no further fuel (2 divided by 3 and rounded down is 0,
# which would call for a negative fuel), so the total fuel required is still just 2. At first, a module of mass 1969
# requires 654 fuel. Then, this fuel requires 216 more fuel (654 / 3 - 2). 216 then requires 70 more fuel,
# which requires 21 fuel, which requires 5 fuel, which requires no further fuel. So, the total fuel required for a
# module of mass 1969 is 654 + 216 + 70 + 21 + 5 = 966. The fuel required by a module of mass 100756 and its fuel is:
# 33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346. What is the sum of the fuel requirements for all of
# the modules on your spacecraft when also taking into account the mass of the added fuel? (Calculate the fuel
# requirements for each module separately, then add them all up at the end.)

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
    while True:
        fuel_needed = (mass // 3) - 2 if ((mass // 3) -2) > 0 else 0
        total_fuel_needed += fuel_needed
        mass = fuel_needed
        if fuel_needed == 0:
            break

print("Result for Advent of Code", total_fuel_needed)

