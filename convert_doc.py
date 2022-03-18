


with open('transfer_file', 'r+', encoding='utf-8') as file:

    lines = file.readlines()
    file.seek(0)
    for line in lines:
        line = line.rstrip('\n')
        x = line.split(", ")
        file.write('<tr><td>' + x[0] + '</td><td>' + x[1] + '</td></tr>\n')
