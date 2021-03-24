fruits = ["orange", "banana","apple","mango"]
print(fruits)


#list() constructor
friuts  = list(("lemon", "banana", "apple", "mango"))
print(friuts)

list1 = ["apple", "banana", "cherry", "orange"] 

list2 = [1, 2, 3, 4, 6, 89, 90]

list3 = [True, False, False ]

list4 = ["apple", 46,True, "john0"]

#list inside a list
list1 = ["john", 45,True]
print(list1)

#accessing item
print(list1[-1])

frs = ["apple", "banana", "cherry"]
if"apple" in friuts:
  print("yes, 'apple'is in the fruits list")
  print("no, 'mango'is in the fruits list")

  fruits = ["apple","banana", "cherry", "orange", "kiwi"]
  fruits[1] = "blackcurrant" #change the second term
  print(fruits)

  fruits[1:3] = ["watermeon"] #changing the second and the third value by replacing it with one value

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

#print all items in the lists, one by one

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

  #use the range() and left() functions to create a create suitable iterable
for i in range (len(fruits)):
 print(fruits[i])