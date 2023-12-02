with open('day2.txt') as prompt:
  games = {int(game.split(':')[0].split(' ')[1]):game.split(':')[1].strip() for game in prompt.read().splitlines()}

valid_limits = {'red': 12, 'green': 13, 'blue': 14}
valid_ids, powers = [], []

for game in games:
  maxes = {'red': 0, 'green': 0, 'blue': 0}
  valid = True
  pulls = games[game].split('; ')
  for pull in pulls:
    for color_group in pull.split(', '):
      number_color = color_group.split(' ')
      if int(number_color[0]) > valid_limits[number_color[1]]:
        valid = False
      if int(number_color[0]) > maxes[number_color[1]]:
        maxes[number_color[1]] = int(number_color[0])
  if valid:
    valid_ids.append(game)
  power = maxes['red'] * maxes['green'] * maxes['blue']
  powers.append(power)

print('part 1:', sum(valid_ids))
print('part 2:', sum(powers))
