if __name__ == "__main__":
 a = 1
 b = 2
add_module = __import__("add_0")
result = add_module.add(a,b)
print("a = {} and b = {} FAKE add () => {} - {}".format(a,b,a,b))