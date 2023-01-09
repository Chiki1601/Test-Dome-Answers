def unique_names(names1, names2):
    set1 = set()
    set1.update(names1,names2)
    return list(set1)
    #return set(names1 + names2)

names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]
print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia
