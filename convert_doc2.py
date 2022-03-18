
with open('fav_temp', 'r+', encoding='utf-8') as file:

    lines = file.readlines()
    file.seek(0)
    for line in lines:
        line = line.rstrip('\n')
        x = line.split(", ")
        file.write('  p'+x[0]+': {\n   title: "'+x[1]+'"\n   addr: "'+x[2]+'"\n   desc: "'+x[3]+'"\n   date: "'+x[4]+'"\n   type: "'+x[5]+'"\n   sites: "'+x[6]+'"\n},\n')

