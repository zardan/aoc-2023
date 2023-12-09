import unittest
import collections

# red, green, blue

colors = {"red": 12, "green": 13, "blue": 14}

file = open("input")
games = file.read().split("\n")

test_file = open("test_input")
test_games = test_file.read().split("\n")

def parse_line(line):
    [game, cubes] = line.split(": ")
    draws = cubes.split("; ")
    max_colors = collections.defaultdict(lambda:0)
    for draw in draws:
        cubes = draw.split(", ")
        for cube in cubes:
            [no, col] = cube.split(" ")
            no = int(no)
            max_colors[col] = max(max_colors[col], no)
    return max_colors

def parse_game_id(line):
    semicolon_index = line.index(":")
    game_index = line[5:semicolon_index]
    game_index = int(game_index)
    return game_index

def is_game_feasible(max_colors):
    feasible = True
    for [color, number] in max_colors.items():
        if max_colors[color] > colors[color]:
            feasible = False
    return feasible

def fewest_cubes(line):
    [game, cubes] = line.split(": ")
    draws = cubes.split("; ")
    fewest_cubes = collections.defaultdict(lambda:0)
    for draw in draws:
        cubes = draw.split(", ")
        for cube in cubes:
            [no, col] = cube.split(" ")
            no = int(no)
            fewest_cubes[col] = max(fewest_cubes[col], no)
    return fewest_cubes

sum_of_ids_part_1 = 0
sum_of_ids_part_2 = 0
for game in games:
    max_colors = parse_line(game)
    game_id = parse_game_id(game)
    if is_game_feasible(max_colors): 
        sum_of_ids_part_1 += game_id
    power_of_set = 1
    for val in max_colors.values():
        power_of_set = power_of_set * val
    sum_of_ids_part_2 += power_of_set

sum_of_products = 0

print("PART 1. ", sum_of_ids_part_1)

print("PART 2. ", sum_of_ids_part_2)


# TESTS

class Test(unittest.TestCase):

    def test_is_game_feasible(self):
        self.assertEqual(
            True,
            is_game_feasible({"red": 4, "green": 2, "blue": 6})
        )
        self.assertEqual(
            False,
            is_game_feasible({"red": 44, "blue": 6})
        )
        self.assertEqual(
            False,
            is_game_feasible({"red": 4, "green": 2, "blue": 100})
        )

    def test_parse_line(self):
        self.assertEqual(
            {"red": 4, "green": 2, "blue": 6}, 
            parse_line(test_games[0])
        )

    def test_parse_game_id(self):
        self.assertEqual(
            1,
            parse_game_id("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
        )

    def test_parse_game_id_is_large(self):
        self.assertEqual(
            200001,
            parse_game_id("Game 200001: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
        )

unittest.main()