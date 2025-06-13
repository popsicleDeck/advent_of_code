from a1_1 import l_list, r_list
# check for duplicates in the left list by comparing len() of og vs len after set(): no dup
#converting the r_list to a dictionary using count() to count occurences and add that value as the value, and key as the number
r_dict = {}
for i in r_list:
    r_dict[i] = r_list.count(i)

#cal sum
similarity_score = 0
for i in l_list: 
    if i in r_dict:
    #how to key get the value of a key in r_dict? forgot syntax
        similarity_score += i * r_dict[i]
print(similarity_score)








