#find the next file number which doesn't exist yet
for i in range(100):
    try:
        file = open(f"file_{i}", "x") #"x" = new file
        print(f"Opened File file_{i}")
    except FileExistsError:
        print(f"File file_{i} exists, trying next...")
