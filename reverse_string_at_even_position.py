"""
example
INPUT:"this is my linked_in post "
OUTPUT :"this si my ni_deknil post  "
"""

str1 = "this is my linked_in post"
li = list(str1.split(" "))
li.append(" ")
print(li)

listOdd = li[1::2]
res= [i[::-1] for i in listOdd]
listEven = li[::2]

def countList(lst1, lst2):
    return [sub[item] for item in range(len(lst2))
            for sub in [lst1, lst2]]


newlist = countList(listEven,res)
def listToString(s):
    return ' '.join(newlist)
print(listToString(newlist))


