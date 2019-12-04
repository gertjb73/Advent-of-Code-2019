# --- Day 3: Crossed Wires ---
# --- Part Two ---
#
# It turns out that this circuit is very timing-sensitive; you actually need to minimize the signal delay.
#
# To do this, calculate the number of steps each wire takes to reach each intersection; choose the intersection where
# the sum of both wires' steps is lowest. If a wire visits a position on the grid multiple times, use the steps value
# from the first time it visits that position when calculating the total value of a specific intersection.
#
# The number of steps a wire takes is the total number of grid squares the wire has entered to get to that location,
# including the intersection being considered. Again consider the example from above:
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

# In the above example, the intersection closest to the central port is reached after 8+5+5+2 = 20 steps by the first
# wire and 7+6+4+3 = 20 steps by the second wire for a total of 20+20 = 40 steps.
#
# However, the top-right intersection is better: the first wire takes only 8+5+2 = 15 and the second wire takes only
# 7+6+2 = 15, a total of 15+15 = 30 steps.
#
# Here are the best steps for the extra examples from above:
#
# R75,D30,R83,U83,L12,D49,R71,U7,L72
# U62,R66,U55,R34,D71,R55,D58,R83 = 610 steps
# R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
# U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = 410 steps
# What is the fewest combined steps the wires must take to reach an intersection?
#
# Puzzle input:
#
# R999,D467,L84,D619,L49,U380,R287,U80,R744,D642,L340,U738,R959,U710,R882,U861,L130,D354,L579,D586,R798,D735,L661,
# D453,L828,U953,R604,D834,R921,D348,R620,U775,R364,U552,L221,U119,R590,U29,L267,D745,L128,U468,L978,D717,R883,D227,
# R691,D330,L33,U520,L862,D132,R99,U400,L455,U737,L603,U220,L689,U131,R158,D674,R617,D287,R422,U734,L73,U327,L525,
# D245,R849,D692,R114,U136,R762,D5,R329,U429,L849,U748,R816,U556,R614,D412,R416,D306,R307,U826,R880,U936,L164,U984,
# L689,D934,R790,D14,R561,D736,L3,D442,R301,D520,L451,U76,R844,D307,L144,D800,L462,D138,R956,U225,L393,D186,L924,
# D445,L86,D640,L920,D877,L197,U191,L371,D701,R826,D282,R856,D412,L788,D417,R69,D678,R978,D268,L268,U112,L69,U164,
# L748,U191,R227,D227,R59,U749,R134,U779,R865,U247,R55,D567,R821,U799,R937,D942,L445,D571,R685,D111,R107,D769,R269,
# D968,R102,U335,R538,U125,L725,D654,R451,D242,R777,U813,R799,D786,L804,U313,L322,U771,R219,U316,L973,U963,R84,D289,
# R825,D299,L425,D49,R995,D486,R550,D789,R735,D501,R966,U955,R432,U635,L353,D600,R675,D236,R864,U322,R719,D418,L877,
# U833,R839,D634,L533,D438,L734,U130,L578,U498,L984,D413,L615,U40,L699,U656,L653,U419,R856,U882,R30,D266,R386,D692,
# L210,U802,L390,U753,L406,U338,R743,D320,L125,U204,R391,U537,R887,D194,L302,U400,R510,U92,L310,D382,R597,U498,R851,
# D357,L568,U800,R918,D106,R673,D735,L86,D67,R398,D677,R355,D501,L909,D133,R729,D293,L498,U222,R832,U671,R751,U36,
# R422,U840,L636,D476,L292,D105,L239,U199,R669,U736,L345,D911,L277,U452,L979,D153,R882,U604,R602,U495,L311,U453,L215,
# D713,R873

# L996,U773,L865,D472,L988,D570,L388,U458,L87,U885,L115,U55,R75,U582,R695,U883,R83,U285,R96,D244,L647,D359,R136,U107,
# R912,U871,L844,U395,L63,U899,L205,D137,R549,U221,L859,D429,L809,U127,R304,U679,L511,U144,R926,U95,L805,U811,R42,
# D248,L546,D644,L551,D897,R368,D391,L224,U164,L490,D991,L146,D615,R536,U247,R10,U998,L957,D233,R706,D926,R760,U438,
# R270,D983,R134,U738,L262,U301,L480,D635,L702,D715,R479,U500,R19,D291,R368,U203,R305,D999,R106,U355,L683,D298,R90,
# U968,L254,D936,R89,U496,R253,U688,R99,U637,L783,D451,R673,D762,R997,D50,L488,U551,L871,U388,R949,D371,R584,D908,
# L880,U523,R557,U436,R520,U587,L56,U18,R397,U541,R660,D444,R51,U187,R221,U902,R726,U303,R97,D817,R185,D218,L240,D67,
# L259,U334,R821,U629,R21,D970,R282,U155,R555,D678,L99,D570,R863,D405,R941,U584,L303,D109,L871,U180,R595,D226,L670,
# D943,L127,U647,R452,D570,R75,D284,R414,U404,R515,U993,R408,U488,R890,D318,L415,U969,R769,D976,L732,U1,R489,U655,
# R930,U638,R649,D254,R161,U287,L659,D26,L477,D821,L124,U538,R17,D711,L203,U888,R904,U648,L908,D65,L215,U283,R698,
# U28,R72,U214,R499,D89,R489,D58,R949,D91,L710,U960,L755,D402,L27,D873,R61,U607,R57,D548,R369,U622,L244,U19,R61,D606,
# R928,D968,R10,D988,R816,U500,R915,D400,R546,D283,L627,D919,L259,U337,R374,U795,L355,D989,L224,D77,L872,U901,R476,
# U765,L320,U768,L937,D437,R141,D822,L326,D324,L498,U994,L518,D857,R973,D681,L710,D590,L879,U499,R488,D151,L242,U988,
# L944,U683,L24,U491,R823,D246,R872,D654,R28,U581,L142,U31,R435,D686,L147,D102,R952,D607,L959,D929,L46


wiremap1 = []
wiremap2 = []

path_test1 = ['R5', 'U5', 'L9', 'D9', 'R3']
path_test2 = ['U3', 'L5', 'D6', 'R3', 'D2']

path_sample1 = ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72']
path_sample2 = ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']

path_sample3 = ['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51']
path_sample4 = ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']

path_puzzle1 = [
    'R999', 'D467', 'L84', 'D619', 'L49', 'U380', 'R287', 'U80', 'R744', 'D642', 'L340', 'U738', 'R959', 'U710', 'R882',
    'U861', 'L130', 'D354', 'L579', 'D586', 'R798', 'D735', 'L661', 'D453', 'L828', 'U953', 'R604', 'D834', 'R921',
    'D348', 'R620', 'U775', 'R364', 'U552', 'L221', 'U119', 'R590', 'U29', 'L267', 'D745', 'L128', 'U468', 'L978',
    'D717', 'R883', 'D227', 'R691', 'D330', 'L33', 'U520', 'L862', 'D132', 'R99', 'U400', 'L455', 'U737', 'L603',
    'U220', 'L689', 'U131', 'R158', 'D674', 'R617', 'D287', 'R422', 'U734', 'L73', 'U327', 'L525', 'D245', 'R849',
    'D692', 'R114', 'U136', 'R762', 'D5', 'R329', 'U429', 'L849', 'U748', 'R816', 'U556', 'R614', 'D412', 'R416',
    'D306', 'R307', 'U826', 'R880', 'U936', 'L164', 'U984', 'L689', 'D934', 'R790', 'D14', 'R561', 'D736', 'L3', 'D442',
    'R301', 'D520', 'L451', 'U76', 'R844', 'D307', 'L144', 'D800', 'L462', 'D138', 'R956', 'U225', 'L393', 'D186',
    'L924', 'D445', 'L86', 'D640', 'L920', 'D877', 'L197', 'U191', 'L371', 'D701', 'R826', 'D282', 'R856', 'D412',
    'L788', 'D417', 'R69', 'D678', 'R978', 'D268', 'L268', 'U112', 'L69', 'U164', 'L748', 'U191', 'R227', 'D227', 'R59',
    'U749', 'R134', 'U779', 'R865', 'U247', 'R55', 'D567', 'R821', 'U799', 'R937', 'D942', 'L445', 'D571', 'R685',
    'D111', 'R107', 'D769', 'R269', 'D968', 'R102', 'U335', 'R538', 'U125', 'L725', 'D654', 'R451', 'D242', 'R777',
    'U813', 'R799', 'D786', 'L804', 'U313', 'L322', 'U771', 'R219', 'U316', 'L973', 'U963', 'R84', 'D289', 'R825',
    'D299', 'L425', 'D49', 'R995', 'D486', 'R550', 'D789', 'R735', 'D501', 'R966', 'U955', 'R432', 'U635', 'L353',
    'D600', 'R675', 'D236', 'R864', 'U322', 'R719', 'D418', 'L877', 'U833', 'R839', 'D634', 'L533', 'D438', 'L734',
    'U130', 'L578', 'U498', 'L984', 'D413', 'L615', 'U40', 'L699', 'U656', 'L653', 'U419', 'R856', 'U882', 'R30',
    'D266', 'R386', 'D692', 'L210', 'U802', 'L390', 'U753', 'L406', 'U338', 'R743', 'D320', 'L125', 'U204', 'R391',
    'U537', 'R887', 'D194', 'L302', 'U400', 'R510', 'U92', 'L310', 'D382', 'R597', 'U498', 'R851', 'D357', 'L568',
    'U800', 'R918', 'D106', 'R673', 'D735', 'L86', 'D67', 'R398', 'D677', 'R355', 'D501', 'L909', 'D133', 'R729',
    'D293', 'L498', 'U222', 'R832', 'U671', 'R751', 'U36', 'R422', 'U840', 'L636', 'D476', 'L292', 'D105', 'L239',
    'U199', 'R669', 'U736', 'L345', 'D911', 'L277', 'U452', 'L979', 'D153', 'R882', 'U604', 'R602', 'U495', 'L311',
    'U453', 'L215', 'D713', 'R873']
path_puzzle2 = [
    'L996', 'U773', 'L865', 'D472', 'L988', 'D570', 'L388', 'U458', 'L87', 'U885', 'L115', 'U55', 'R75', 'U582', 'R695',
    'U883', 'R83', 'U285', 'R96', 'D244', 'L647', 'D359', 'R136', 'U107', 'R912', 'U871', 'L844', 'U395', 'L63', 'U899',
    'L205', 'D137', 'R549', 'U221', 'L859', 'D429', 'L809', 'U127', 'R304', 'U679', 'L511', 'U144', 'R926', 'U95',
    'L805', 'U811', 'R42', 'D248', 'L546', 'D644', 'L551', 'D897', 'R368', 'D391', 'L224', 'U164', 'L490', 'D991',
    'L146', 'D615', 'R536', 'U247', 'R10', 'U998', 'L957', 'D233', 'R706', 'D926', 'R760', 'U438', 'R270', 'D983',
    'R134', 'U738', 'L262', 'U301', 'L480', 'D635', 'L702', 'D715', 'R479', 'U500', 'R19', 'D291', 'R368', 'U203',
    'R305', 'D999', 'R106', 'U355', 'L683', 'D298', 'R90', 'U968', 'L254', 'D936', 'R89', 'U496', 'R253', 'U688', 'R99',
    'U637', 'L783', 'D451', 'R673', 'D762', 'R997', 'D50', 'L488', 'U551', 'L871', 'U388', 'R949', 'D371', 'R584',
    'D908', 'L880', 'U523', 'R557', 'U436', 'R520', 'U587', 'L56', 'U18', 'R397', 'U541', 'R660', 'D444', 'R51', 'U187',
    'R221', 'U902', 'R726', 'U303', 'R97', 'D817', 'R185', 'D218', 'L240', 'D67', 'L259', 'U334', 'R821', 'U629', 'R21',
    'D970', 'R282', 'U155', 'R555', 'D678', 'L99', 'D570', 'R863', 'D405', 'R941', 'U584', 'L303', 'D109', 'L871',
    'U180', 'R595', 'D226', 'L670', 'D943', 'L127', 'U647', 'R452', 'D570', 'R75', 'D284', 'R414', 'U404', 'R515',
    'U993', 'R408', 'U488', 'R890', 'D318', 'L415', 'U969', 'R769', 'D976', 'L732', 'U1', 'R489', 'U655', 'R930',
    'U638', 'R649', 'D254', 'R161', 'U287', 'L659', 'D26', 'L477', 'D821', 'L124', 'U538', 'R17', 'D711', 'L203',
    'U888', 'R904', 'U648', 'L908', 'D65', 'L215', 'U283', 'R698', 'U28', 'R72', 'U214', 'R499', 'D89', 'R489', 'D58',
    'R949', 'D91', 'L710', 'U960', 'L755', 'D402', 'L27', 'D873', 'R61', 'U607', 'R57', 'D548', 'R369', 'U622', 'L244',
    'U19', 'R61', 'D606', 'R928', 'D968', 'R10', 'D988', 'R816', 'U500', 'R915', 'D400', 'R546', 'D283', 'L627', 'D919',
    'L259', 'U337', 'R374', 'U795', 'L355', 'D989', 'L224', 'D77', 'L872', 'U901', 'R476', 'U765', 'L320', 'U768',
    'L937', 'D437', 'R141', 'D822', 'L326', 'D324', 'L498', 'U994', 'L518', 'D857', 'R973', 'D681', 'L710', 'D590',
    'L879', 'U499', 'R488', 'D151', 'L242', 'U988', 'L944', 'U683', 'L24', 'U491', 'R823', 'D246', 'R872', 'D654',
    'R28', 'U581', 'L142', 'U31', 'R435', 'D686', 'L147', 'D102', 'R952', 'D607', 'L959', 'D929', 'L46']


# Function to plot given path on plottedmap
def plot_path(path, plottedmap):
    plottedmap.append({'x': 0, 'y': 0})
    print('Path to plot:', path)
    pos_x = pos_y = 0
    for step in path:
        # R and L adjust the width, U and D adjust the height
        if step[0] == 'R':
            for i in range(int(step[1:])):
                plottedmap.append({'x': pos_x + (i + 1), 'y': pos_y})
            pos_x += int(step[1:])
        if step[0] == 'L':
            for i in range(int(step[1:])):
                plottedmap.append({'x': pos_x - (i + 1), 'y': pos_y})
            pos_x -= int(step[1:])
        if step[0] == 'U':
            for i in range(int(step[1:])):
                plottedmap.append({'x': pos_x, 'y': pos_y + (i + 1)})
            pos_y += int(step[1:])
        if step[0] == 'D':
            for i in range(int(step[1:])):
                plottedmap.append({'x': pos_x, 'y': pos_y - (i + 1)})
            pos_y -= int(step[1:])
    return


# Function to find wire crossings
def find_wire_crossings(plottedmap1, plottedmap2):
    i = 0
    print('\nFind wire crossings')
    mapequal = []
    for coord1 in plottedmap1:
        for coord2 in plottedmap2:
            i += 1
            if coord1 == coord2:
                mapequal.append(coord1)
                print(coord1)
    return mapequal


def find_distance_to_closest_crossing(list_of_crossings):
    print('\nDetermine distance to closest crossing')
    min_dist = 0
    for crossing in list_of_crossings:
        x = abs(crossing.get('x'))
        y = abs(crossing.get('y'))
        distance = x + y
        if distance != 0:
            if min_dist == 0:
                min_dist = distance
            min_dist = distance if distance < min_dist else min_dist
        print('Distance:', x, '+', y, '=', distance, ')')
    return min_dist


def find_shortest_distance_to_crossing(plottedmap1, plottedmap2, crossings):
    min_steps_needed = 0
    for crossing in crossings:
        steps_taken = 0
        for step in plottedmap1:
            if crossing == step:
                break
            steps_taken += 1
        for step in plottedmap2:
            if crossing == step:
                break
            steps_taken += 1
        if min_steps_needed == 0:
            min_steps_needed = steps_taken
        print('Steps taken:', steps_taken)
        min_steps_needed = steps_taken if steps_taken < min_steps_needed else min_steps_needed
    return min_steps_needed


plot_path(path_puzzle1, wiremap1)
plot_path(path_puzzle2, wiremap2)

# I still have the list of crossings from last exercise.
# Determining it this way is very time consuming
# So for a shortcut I hard-coded them
# # # crossings = find_wire_crossings(wiremap1, wiremap2)

crossings = [
    {'x': 6491, 'y': 1524},
    {'x': 6769, 'y': 1619},
    {'x': 6788, 'y': 1619},
    {'x': 7028, 'y': 1619},
    {'x': 7371, 'y': 2377},
    {'x': 7207, 'y': 2660},
    {'x': 6518, 'y': 3060},
    {'x': 7655, 'y': 2591}]

minimum_distance = find_distance_to_closest_crossing(crossings)
print('Minimum distance is', minimum_distance, '\n')

minimum_steps_needed = find_shortest_distance_to_crossing(wiremap1, wiremap2, crossings)
print('Minimum steps needed is', minimum_steps_needed)

# /usr/local/bin/python3.7 "/Users/rx05sx/Documents/Advent of Code/2019/Day3_Part1.py"
# 301
# 301
# Path to plot: ['R999', 'D467', 'L84', 'D619', 'L49', 'U380', 'R287', 'U80', 'R744', 'D642', 'L340', 'U738', 'R959', 'U710', 'R882', 'U861', 'L130', 'D354', 'L579', 'D586', 'R798', 'D735', 'L661', 'D453', 'L828', 'U953', 'R604', 'D834', 'R921', 'D348', 'R620', 'U775', 'R364', 'U552', 'L221', 'U119', 'R590', 'U29', 'L267', 'D745', 'L128', 'U468', 'L978', 'D717', 'R883', 'D227', 'R691', 'D330', 'L33', 'U520', 'L862', 'D132', 'R99', 'U400', 'L455', 'U737', 'L603', 'U220', 'L689', 'U131', 'R158', 'D674', 'R617', 'D287', 'R422', 'U734', 'L73', 'U327', 'L525', 'D245', 'R849', 'D692', 'R114', 'U136', 'R762', 'D5', 'R329', 'U429', 'L849', 'U748', 'R816', 'U556', 'R614', 'D412', 'R416', 'D306', 'R307', 'U826', 'R880', 'U936', 'L164', 'U984', 'L689', 'D934', 'R790', 'D14', 'R561', 'D736', 'L3', 'D442', 'R301', 'D520', 'L451', 'U76', 'R844', 'D307', 'L144', 'D800', 'L462', 'D138', 'R956', 'U225', 'L393', 'D186', 'L924', 'D445', 'L86', 'D640', 'L920', 'D877', 'L197', 'U191', 'L371', 'D701', 'R826', 'D282', 'R856', 'D412', 'L788', 'D417', 'R69', 'D678', 'R978', 'D268', 'L268', 'U112', 'L69', 'U164', 'L748', 'U191', 'R227', 'D227', 'R59', 'U749', 'R134', 'U779', 'R865', 'U247', 'R55', 'D567', 'R821', 'U799', 'R937', 'D942', 'L445', 'D571', 'R685', 'D111', 'R107', 'D769', 'R269', 'D968', 'R102', 'U335', 'R538', 'U125', 'L725', 'D654', 'R451', 'D242', 'R777', 'U813', 'R799', 'D786', 'L804', 'U313', 'L322', 'U771', 'R219', 'U316', 'L973', 'U963', 'R84', 'D289', 'R825', 'D299', 'L425', 'D49', 'R995', 'D486', 'R550', 'D789', 'R735', 'D501', 'R966', 'U955', 'R432', 'U635', 'L353', 'D600', 'R675', 'D236', 'R864', 'U322', 'R719', 'D418', 'L877', 'U833', 'R839', 'D634', 'L533', 'D438', 'L734', 'U130', 'L578', 'U498', 'L984', 'D413', 'L615', 'U40', 'L699', 'U656', 'L653', 'U419', 'R856', 'U882', 'R30', 'D266', 'R386', 'D692', 'L210', 'U802', 'L390', 'U753', 'L406', 'U338', 'R743', 'D320', 'L125', 'U204', 'R391', 'U537', 'R887', 'D194', 'L302', 'U400', 'R510', 'U92', 'L310', 'D382', 'R597', 'U498', 'R851', 'D357', 'L568', 'U800', 'R918', 'D106', 'R673', 'D735', 'L86', 'D67', 'R398', 'D677', 'R355', 'D501', 'L909', 'D133', 'R729', 'D293', 'L498', 'U222', 'R832', 'U671', 'R751', 'U36', 'R422', 'U840', 'L636', 'D476', 'L292', 'D105', 'L239', 'U199', 'R669', 'U736', 'L345', 'D911', 'L277', 'U452', 'L979', 'D153', 'R882', 'U604', 'R602', 'U495', 'L311', 'U453', 'L215', 'D713', 'R873']
# Path to plot: ['L996', 'U773', 'L865', 'D472', 'L988', 'D570', 'L388', 'U458', 'L87', 'U885', 'L115', 'U55', 'R75', 'U582', 'R695', 'U883', 'R83', 'U285', 'R96', 'D244', 'L647', 'D359', 'R136', 'U107', 'R912', 'U871', 'L844', 'U395', 'L63', 'U899', 'L205', 'D137', 'R549', 'U221', 'L859', 'D429', 'L809', 'U127', 'R304', 'U679', 'L511', 'U144', 'R926', 'U95', 'L805', 'U811', 'R42', 'D248', 'L546', 'D644', 'L551', 'D897', 'R368', 'D391', 'L224', 'U164', 'L490', 'D991', 'L146', 'D615', 'R536', 'U247', 'R10', 'U998', 'L957', 'D233', 'R706', 'D926', 'R760', 'U438', 'R270', 'D983', 'R134', 'U738', 'L262', 'U301', 'L480', 'D635', 'L702', 'D715', 'R479', 'U500', 'R19', 'D291', 'R368', 'U203', 'R305', 'D999', 'R106', 'U355', 'L683', 'D298', 'R90', 'U968', 'L254', 'D936', 'R89', 'U496', 'R253', 'U688', 'R99', 'U637', 'L783', 'D451', 'R673', 'D762', 'R997', 'D50', 'L488', 'U551', 'L871', 'U388', 'R949', 'D371', 'R584', 'D908', 'L880', 'U523', 'R557', 'U436', 'R520', 'U587', 'L56', 'U18', 'R397', 'U541', 'R660', 'D444', 'R51', 'U187', 'R221', 'U902', 'R726', 'U303', 'R97', 'D817', 'R185', 'D218', 'L240', 'D67', 'L259', 'U334', 'R821', 'U629', 'R21', 'D970', 'R282', 'U155', 'R555', 'D678', 'L99', 'D570', 'R863', 'D405', 'R941', 'U584', 'L303', 'D109', 'L871', 'U180', 'R595', 'D226', 'L670', 'D943', 'L127', 'U647', 'R452', 'D570', 'R75', 'D284', 'R414', 'U404', 'R515', 'U993', 'R408', 'U488', 'R890', 'D318', 'L415', 'U969', 'R769', 'D976', 'L732', 'U1', 'R489', 'U655', 'R930', 'U638', 'R649', 'D254', 'R161', 'U287', 'L659', 'D26', 'L477', 'D821', 'L124', 'U538', 'R17', 'D711', 'L203', 'U888', 'R904', 'U648', 'L908', 'D65', 'L215', 'U283', 'R698', 'U28', 'R72', 'U214', 'R499', 'D89', 'R489', 'D58', 'R949', 'D91', 'L710', 'U960', 'L755', 'D402', 'L27', 'D873', 'R61', 'U607', 'R57', 'D548', 'R369', 'U622', 'L244', 'U19', 'R61', 'D606', 'R928', 'D968', 'R10', 'D988', 'R816', 'U500', 'R915', 'D400', 'R546', 'D283', 'L627', 'D919', 'L259', 'U337', 'R374', 'U795', 'L355', 'D989', 'L224', 'D77', 'L872', 'U901', 'R476', 'U765', 'L320', 'U768', 'L937', 'D437', 'R141', 'D822', 'L326', 'D324', 'L498', 'U994', 'L518', 'D857', 'R973', 'D681', 'L710', 'D590', 'L879', 'U499', 'R488', 'D151', 'L242', 'U988', 'L944', 'U683', 'L24', 'U491', 'R823', 'D246', 'R872', 'D654', 'R28', 'U581', 'L142', 'U31', 'R435', 'D686', 'L147', 'D102', 'R952', 'D607', 'L959', 'D929', 'L46']
# 153537
# 149380
#
# Find wire crossings
# {'x': 0, 'y': 0}
# {'x': 6491, 'y': 1524}
# {'x': 6769, 'y': 1619}
# {'x': 6788, 'y': 1619}
# {'x': 7028, 'y': 1619}
# {'x': 7371, 'y': 2377}
# {'x': 7207, 'y': 2660}
# {'x': 6518, 'y': 3060}
# {'x': 7655, 'y': 2591}
#
# Determine distance to closest crossing
# Distance: 0 + 0 = 0 )
# Distance: 6491 + 1524 = 8015 )
# Distance: 6769 + 1619 = 8388 )
# Distance: 6788 + 1619 = 8407 )
# Distance: 7028 + 1619 = 8647 )
# Distance: 7371 + 2377 = 9748 )
# Distance: 7207 + 2660 = 9867 )
# Distance: 6518 + 3060 = 9578 )
# Distance: 7655 + 2591 = 10246 )
# Minimum distance is 8015
