with open('day1.txt') as prompt:
  lines = prompt.read().splitlines()

part_1_calibration_values = []

for line in lines:
  numbers = list(filter(str.isdigit, line))
  if len(numbers) == 1:
    part_1_calibration_values.append(numbers[0] + numbers[0])
  else:
    part_1_calibration_values.append(numbers[0] + numbers[-1])

print("part 1:", sum(map(int, part_1_calibration_values)))

part_2_calibration_values = []

number_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

for line in lines:
  numbers = []
  for idx, character in enumerate(line):
    if character.isdigit():
      numbers.append(character)
    else:
      for end_point in range(4, 1, -1):
        if idx < len(line) - end_point:
          substr = line[idx:idx + end_point + 1]
          if substr in number_dict:
            numbers.append(number_dict[substr])
  if len(numbers) == 1:
    part_2_calibration_values.append(numbers[0] + numbers[0])
  else:
    part_2_calibration_values.append(numbers[0] + numbers[-1])

print("part 2:", sum(map(int, part_2_calibration_values)))