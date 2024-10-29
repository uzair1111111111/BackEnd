cool_beasts = {"octopuces": "tentacles", "dolphins": "fins", "rhinos": "horns"}

for animal, feature in cool_beasts.items():
    print("{} have {}".format(animal, feature))

a=0/5
print(a)    
def divide_by(a,b):
    return a/b
try:
    ans=divide_by(40,0)
except Exception as e:
    print("something went wrong!",e)    
    print(e.__class__)
try:
     items=[1,2,3,4,5]
     item=items[5]

     print(item)
except:
    print('non')   
#MAP FILTER
menu=["octopuces", "tentacles", "dolphins", "fins", "rhinos", "horns"]    
def find_animal(animal):
    if animal[0]=='t':
        return animal
filter_animal=filter(find_animal,menu)    
print(filter_animal)
for x in filter_animal:
    print(x)  

