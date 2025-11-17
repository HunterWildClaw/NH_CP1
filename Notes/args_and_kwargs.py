# NH 2nd args and kwargs notes

"""def hello(name="Tia", age=29):
    return f"Hello {name}! You are {age}!"

print(hello())
print(hello("Xavier"))
print(hello(age = 19, name="Treyson"))"""

# postitional arguments, *args, Keywords arguments, **kwargs
def hello(*names, **last):
    print(type(names))
    for name in names:
        if name == "Vienna":
            print(f"Hello {name} {last['alast']} {last['vlast']} ")
        else:
            print(f"Hello {name} {last['alast']}")

hello("LaRose", "Alexander", "Kathryn", "Andrew", "Vienna", "Victoria", "Treyson", "Xavier", "Jake", alast = "LaRose", vlast="Atkin")