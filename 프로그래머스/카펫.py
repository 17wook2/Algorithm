def solution(brown, yellow):
    row_plus_column = (brown + 4) // 2
    row_mul_column = yellow - 4 + 2 * row_plus_column
    x=0
    y=0
    print(row_plus_column,row_mul_column)
    for row in range(1,int(row_plus_column//2)+1):
        column = row_plus_column - row
        if row * column == row_mul_column:
            x = row
            y = column
            break
    if x < y:
        x,y = y,x
    return [x,y]