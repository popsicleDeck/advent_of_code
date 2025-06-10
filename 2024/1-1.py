#handling input
input_ = open("/home/chau/Projects/AdventOfCode/2024/1-1-input.txt", "r").read()
input_ = input_.replace("\n", " ")
input_ = input_.split(" ")
input_ = [j for _,j in enumerate(input_) if j != '']

l_list = [j for i,j in enumerate(input_) if i % 2 == 0]
r_list = [j for i,j in enumerate(input_) if i % 2 != 0]

l_list = list(map(int, l_list))
r_list = list(map(int, r_list))

#sorting
l_list.sort()
r_list.sort()

input_ = list(zip(l_list, r_list))

#calculation
sum = 0
for i in range(len(input_)):
    sum += abs(input_[i][0] - input_[i][1])
    i += 1
print(sum)


