import unittest
import collections

# red, green, blue

colors = {"red": 12, "green": 13, "blue": 14}

file = open("input")
games = file.read()
games = games.split("\n")

file = open("test_input")
test_games = file.read().split("\n")

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

sum_of_ids = 0
for game in games:
    max_colors = parse_line(game)
    game_id = parse_game_id(game)
    if is_game_feasible(max_colors): 
        sum_of_ids += game_id
        
print(sum_of_ids)

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