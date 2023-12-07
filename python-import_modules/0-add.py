if __name__ == "__main__":
 import add_0

 a = 1
 b = 2

result = add_0.add(a,b)
print("a = {} and b = {} FAKE add() => {} - {}".format(a,b,a,b))

a = 10
b = 30

result = add_0.add(a,b)
print("a = {} and b = {} FAKE add() => {} - {}".format(a,b,a,b))

a = -10
b = 30

result = add_0.add(a,b)
print("a = {} and b = {} FAKE add() => {} - {}".format(a,b,a,b))

a = 5
b = "H"

result = add_0.add(a,b)
print("a = {} and b = {} FAKE add() => {} - {}".format(a,b,a,b))