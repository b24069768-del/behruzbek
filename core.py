x=int(input("x sonini kiriting"))
y=int(input("y sonini kiriting"))
z=int(input("z sonini kiriting"))
if (x > y and y > z) or (x > z and z > y):
    print("Eng katta son x: ",x)
elif (y > x and x > z) or (y > z and z > y):
    print("Eng katta son y: ",y)
elif(z > x and x > y ) or (z > y and y > x):
    print("Eng katta son z: ",z)
else:
    print("Bu sonlar bir-biriga teng")
