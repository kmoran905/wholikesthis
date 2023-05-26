def likes(names):
    count = len(names)
    if count >= 4:
        return names[0] + ", " + names[1] + " and " + str(count - 2) +  " others like this"
    elif count == 3:
        return names[0] + ", " + names[1] + " and " + names[2] + " like this"
    elif count == 2:
        return names[0] + " and " + names[1] + " like this"
    elif count == 1:
        return names[0] + " likes this"
    else:
        return "no one likes this"
    

print(likes(["James", "Richard", "Sarah", "Michael"]))