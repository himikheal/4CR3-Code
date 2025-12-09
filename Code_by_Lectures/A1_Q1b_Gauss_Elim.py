# determine if matrix is independent for binary field

def gauss_elimination_binary(matrix):
    n = len(matrix)        # number of equations
    m = len(matrix[0]) - 1 # number of variables

    # Forward elimination
    row = 0
    for col in range(m):
        # Find pivot
        pivot = None
        for r in range(row, n):
            if matrix[r][col] == 1:
                pivot = r
                break
        if pivot is None:
            continue  # No pivot in this column

        # Swap to move pivot to current row
        matrix[row], matrix[pivot] = matrix[pivot], matrix[row]

        # Eliminate below
        for r in range(row + 1, n):
            if matrix[r][col] == 1:
                # XOR row r with pivot row
                matrix[r] = [(a ^ b) for a, b in zip(matrix[r], matrix[row])]

        row += 1
        if row == n:
            break

    # Back substitution
    solution = [0] * m
    for r in range(n - 1, -1, -1):
        # Find leading 1 in row r
        lead = None
        for c in range(m):
            if matrix[r][c] == 1:
                lead = c
                break
        if lead is None:
            # Check if inconsistent (0 = 1)
            if matrix[r][m] == 1:
                return None  # no solution
            continue
        # Calculate solution for variable lead
        val = matrix[r][m]
        for c in range(lead + 1, m):
            val ^= (matrix[r][c] & solution[c])
        solution[lead] = val

    return solution

# put ur matrix here !
keystream = list("00110110010101101111111010110111110111100100001101")
keystream = [int(b) for b in keystream]

# --- Step 3: Build the augmented matrix for 20 unknowns ---
matrix = []
for i in range(20):  # 20 equations
    row = keystream[i:i+20] + [keystream[i+20]]  # 20 inputs + next bit as RHS
    matrix.append(row)

# print(matrix)
# print(len(matrix), len(matrix[0]))

# --- Step 4: Solve for the coefficients ---
solution = gauss_elimination_binary(matrix)

if solution is None:
    print("No solution exists.")
else:
    print("Solution vector:")
    print(solution)