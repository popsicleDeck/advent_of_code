#input handling
input_ = open("/home/chau/Projects/AdventOfCode/2024/a2_1_input.txt", "r").read()
input_ = input_.split("\n") 
#no idea why there's an empty string at the bottom of the list even though I've checked the input file, there's no new line
del input_[-1]
input_ = [input_[i].split(" ") for i in range(len(input_))]
input_ = [list(map(int, i)) for i in input_]

#checking, don't know what to do next
input_ = [i for i in input_ if i == sorted(i) or i == sorted(i, reverse=True)]
#calculating safe_score
