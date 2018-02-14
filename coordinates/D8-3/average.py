




if __name__ == "__main__":
    f = open(input("file name: "))
    size = float(f.readline())
    f.readline()

    x = 0.0
    y = 0.0
    z = 0.0
    for line in f:
        coords = line.split()
        x += float(coords[1])
        y += float(coords[2])
        z += float(coords[3])

    x = x / size
    y = y / size
    z = z / size

    print("midpoint: (%.5f, %.5f, %.5f)" %(x, y, z))
