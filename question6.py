# create a empty dictionary . allow 4 friends to enter their
# favorite language as value and key as their names.assume that 
# the names are unique
d = {}

name = input("enter a name:")
lang = input("enter a language:")
d.update({name:lang})
name = input("enter a name:")
lang = input("enter a language:")
d.update({name:lang})
name = input("enter a name:")
lang = input("enter a language:")
d.update({name:lang})
name = input("enter a name:")
lang = input("enter a language:")
d.update({name:lang})
print(d)