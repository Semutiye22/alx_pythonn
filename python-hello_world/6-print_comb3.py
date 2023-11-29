for i in range(10):
    for j in range(i + 1, 10):
        print(f"{i}{j}" if i != 9 or j != 9 else f"{i}{j}\n", end=", " if i != 8 or j != 9 else "")
  
        