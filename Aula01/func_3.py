def wabbbajack(stuff):

    if isinstance(stuff, int) or isinstance(stuff,float):
        return str(stuff)
    elif isinstance(stuff, str) :
        return len(stuff)
    else:
        "Sorry, that’s not a float or string"


print(wabbbajack(1.2))
print(wabbbajack(5))
print(wabbbajack("HAHAHAHAHADJhajwdhabjdbajn"))

