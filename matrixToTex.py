### convert a matrix into LaTeX code
matrix = []

# get matrix dimensions: r x c
dims = input("pass 2 space-separated numbers for (rows, columns): ").split()

# get matrix
for i in range(int(dims[0])):
    row = input("pass " + dims[1] + " space-separated numbers for row " + str(i + 1) + ": ").split()
    matrix.append(row)

# convert to tex
texCode = "\\begin{bmatrix}"
for row in matrix:
    for num in row:
        texCode += num + "&"
    texCode = texCode[:-1] + "\\\\"

texCode = texCode[:-2] + "\\end{bmatrix}"

# profit
print(texCode)
