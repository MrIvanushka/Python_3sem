line = input()

correct_line = str(line[0].upper())

for i in range(1, len(line)):
    if line[i] == ' ' and line[i+1] < 'A':
        pass
    else:
        if i < 2:
            correct_line += line[i]
        elif line[i-1] < 'A' and line[i-1] > ' ' and line[i] != ' ':
            correct_line += ' '
            if line[i-1] != ',':
                correct_line += line[i].upper()
        elif correct_line[len(correct_line) - 2] < 'A' and correct_line[len(correct_line) - 2] > ' ' and correct_line[len(correct_line) - 2] != ',':
            correct_line += line[i].upper()
        else:
            correct_line += line[i]
print(correct_line)