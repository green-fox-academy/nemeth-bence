fr = open("lotto.csv", "r")

number_dist = [0] * 90

for line in my_file:
    line_list = line.rstrip().split(";")
    for number in line_list[11:16]:
        number_dist[number] += 1
        
print(number_dist)

fr = close
