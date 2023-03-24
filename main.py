# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scorer_name_goal_0 = "Ruud Gullit"
scorer_name_goal_1 = "Marco van Basten"

goal_0 = 32
goal_1 = 54

scorers = scorer_name_goal_0 + " " + \
    str(goal_0) + ", " + scorer_name_goal_1 + " " + str(goal_1)
print(scorers)

# --- This seems to be the same even though it is not accepted by Wincpy ---
# report = f"""{scorer_name_goal_0} scored in the {goal_0}nd minute
# {scorer_name_goal_1} scored in the {goal_1}th minute
# """
report = f"{scorer_name_goal_0} scored in the {goal_0}nd minute" '\n' f"{scorer_name_goal_1} scored in the {goal_1}th minute"
print(report)

player = "Ruud Gullit"
first_name = player[0:player.find(" ")]
print(first_name)
last_name_len = len(player[player.find(" ")+1:])
print(last_name_len)

name_short = f'{first_name[0]}. {player[player.find(" ")+1:]}'
print(name_short)

chant = f"{first_name}! {first_name}! {first_name}! {first_name}!"
# --- This seems to be the same even though it is not accepted by Wincpy ---
# chant = f"{len(first_name) * (first_name + '! ')}"
print(chant)

good_chant = first_name[-1] != " "
print(good_chant)
