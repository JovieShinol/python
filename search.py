def find_max_ones_row(matrix):
    max_ones_row = -1
    max_ones_count = -1

    for i, row in enumerate(matrix):
        ones_count = row.count(1)
        if ones_count > max_ones_count:
            max_ones_count = ones_count
            max_ones_row = i

    return max_ones_row

# Input
test_cases = int(input())
matrix = []

for _ in range(test_cases):
    row = list(map(int, input().split()))
    matrix.append(row)

# Find and print the row with the maximum number of 1's
result = find_max_ones_row(matrix)
print(result)
