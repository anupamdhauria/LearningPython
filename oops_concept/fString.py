val="Geeks"
print (f"{val}for{val} is a portal for {val}")
print("-----------------------------------------------------------------")
name="Tushar"
age=23
print(f"Hello,my name is {name} and I'm {age} years old")
print("-----------------------------------------------------------------")
import datetime
today=datetime.datetime.today();
print(today) #2023-07-12 20:20:17.475931
print(f"{today:%B %d,%Y}") #July 12,2023

print("-----------------------------------------------------------------")
#new line in fstring
n1='\n'
name='anupam'
age=28
print(f"name:{name}{n1}age:{age}")

