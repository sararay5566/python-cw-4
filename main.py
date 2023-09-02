def my_name():
    print("My name is sara")

def my_meal(food,drink):
    print("i like to eat {food} and while drinking{drink}" )

def cube(number):
    return number**3
print(cube(3))
def by_three(number):
    if number %3==0:
        return cube (number)
    else:
        return False
    
print(by_three(4))