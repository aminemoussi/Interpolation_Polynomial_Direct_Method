import numpy as np
import time

def gaussian_elimination(a_matrix, b_matrix):
    if (a_matrix.shape[1] != b_matrix.shape[0]):
        print("Error: rows in A is not equate column in B.")
    elif (b_matrix.shape[1] != 1) or (b_matrix.shape[0] != a_matrix.shape[0]):
        print("Error: number of columns in B does not equate to one, or A is not squared.")


    #creating thre augmented matrix
    augmented_matrix = np.concatenate((a_matrix, b_matrix), axis= 1)

    n = len(b_matrix) #num of rows
    doable = True

    for k in range(n):        #interchanging the rows to eliminate the null pivots
        if augmented_matrix[k][k] == 0:
            for i in range(k + 1, n ):
                if augmented_matrix[i][k] != 0:
                    augmented_matrix[[i, k]] = augmented_matrix[[k, i]]
                    break
                elif i == n :
                    doable = False
                    break


    if not doable :
        print("IMPOSSIBLE: to be done ",k,"th pivot couldn't be fixed.")
        time.sleep(1.5)
    else:
        for i in range(n - 1):
            for j in range(i + 1, n):
                if augmented_matrix[j][i] != 0:
                    scalability_factor = augmented_matrix[j][i] / augmented_matrix[i][i]
                    for k in range(i, n + 1):
                        augmented_matrix[j][k] = augmented_matrix[j][k] - augmented_matrix[i][k] * scalability_factor


    val = find_variables(augmented_matrix, n)

    return val




def find_variables(matrix, n):
    k = n - 1
    values = [1] * n
    while k >= 0:
        denom = 0
        for i in range(n):
            denom = denom + values[i] * matrix[k][i]

        if denom == 0:
            # Handle the case where denom is zero (optional: print a warning)
            print("Warning: Denominator is zero. Setting the corresponding variable to zero.")
            values[k] = 0
        else:
            x = matrix[k][n] / denom
            values[k] = x

        k = k - 1

    return values
