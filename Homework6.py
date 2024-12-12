print("number 1")
def find(matrix):
    max_sum_row = matrix[0]
    min_sum_row = matrix[0]
    max_sum = sum(max_sum_row)
    min_sum = sum(min_sum_row)
    for row in matrix[1:]:
        row_sum = sum(row)
        if row_sum > max_sum:
            max_sum = row_sum
            max_sum_row = row
        if row_sum < min_sum:
            min_sum = row_sum
            min_sum_row = row
    return max_sum_row, max_sum, min_sum_row, min_sum
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]
max_row, max_row_sum, min_row, min_row_sum = find(matrix)
print("Строка с максимальной суммой:", max_row)
print("Сумма элементов этой строки:", max_row_sum)
print("Строка с минимальной суммой:", min_row)
print("Сумма элементов этой строки:", min_row_sum)
print("number 2")
def change_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        min_value = min(matrix[i])
        min_index = matrix[i].index(min_value)
        if min_value % 2 == 0:
            matrix[i][min_index] = 0
        else:
            matrix[i][min_index] = 1

    return matrix
new_matrix = change_matrix(matrix)
for row in new_matrix:
    print(row)