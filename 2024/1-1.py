#handling input
input_ = open("/home/chau/Projects/AdventOfCode/2024/1-1-input.txt", "r").read()
input_ = input_.replace("\n", " ")
input_ = input_.split(" ")
input_ = [j for _,j in enumerate(input_) if j != '']

list_1 = [j for i,j in enumerate(input_) if i % 2 == 0]
list_2 = [j for i,j in enumerate(input_) if i % 2 != 0]

list_1 = list(map(int, list_1))
list_2 = list(map(int, list_2))

#sorting
list_1.sort()
list_2.sort()

input_ = list(zip(list_1, list_2))

#calculation
sum = 0
for i in range(len(input_)):
    sum += abs(input_[i][0] - input_[i][1])
    i += 1
print(sum)


