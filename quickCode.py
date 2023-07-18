with open("animationNames.txt", "r") as file:
    lines = file.readlines()

strings_per_line = 10
formatted_lines = [f'"{line.strip()}",' for line in lines]
formatted_lines_per_line = [formatted_lines[i:i+strings_per_line] for i in range(0, len(formatted_lines), strings_per_line)]

with open("animationNames_formatted.txt", "w") as file:
    for line in formatted_lines_per_line:
        file.write(' '.join(line) + '\n')
