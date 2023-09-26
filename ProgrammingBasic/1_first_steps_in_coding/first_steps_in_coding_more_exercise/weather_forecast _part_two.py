celsius = float(input())

if celsius > float(25.9):
    print("Hot")
elif celsius > float(20):
    print("Warm")
elif celsius > float(14.9):
    print("Mild")
elif celsius > float(11.9):
    print("Cool")
elif celsius > float(4.9):
    print("Cold")
else:
    print("unknown")