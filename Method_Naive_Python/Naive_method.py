import numpy as np
import Gaussian_elem



def print_matrix(m):
    for row in m:
        for elem in row:
            print(elem, end="   ")
        print()


def polynom(result, x):
    return result[0] + result[1]*x + result[2]*(x**2) + result[3]*(x**3)




x0 = 0; x1 = 1; x2 = 2; x3 = 3
y0 = 1; y1 = 0.904837; y2 = 0.818730; y3 = 0.740818

matrix = np.array([
            [1, x0, x0**2, x0**3],
            [1, x1, x1**2, x1**3],
            [1, x2, x2**2, x2**3],
            [1, x3, x3**2, x3**3]
                ]
        )

output = np.array([
    [y0],
    [y1],
    [y2],
    [y3]
])

result = Gaussian_elem.gaussian_elimination(matrix, output)

print("The polynom's coef:")
i=0
for elem in result:
    print("a", i, " = ", elem)
    i += 1

print("The approximate value of f(1.5) using the Naive method is: f(1.5) = ", polynom(result, 1.5))