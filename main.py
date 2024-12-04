

# We are given a search input where any letters that are not X M A S are irrelevant.
# within those letters that are left we have to find the word "XMAS" which could be horizontal, vertical, diagonal, written backwards, or even overlapping other words.
# We have to find all of them and count

def main():
    input = open("input.txt", "r")

    # read the input as a matrix of characters where num of columns = input line length

    line = input.readline().strip()
    
    matrix = []
    while line:
        matrix.append(list(line))
        line = input.readline().strip()

    for i in range(len(matrix)):
        print(matrix[i])

    print()

    # search for XMAS in all directions
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'X':
                #left-to-right
                if j + 3 < len(matrix[i]) and matrix[i][j+1] == 'M' and matrix[i][j+2] == 'A' and matrix[i][j+3] == 'S':
                    count += 1
                    print("Found XMAS at", i, j, "horizontal left-to-right")
                # right-to-left
                if j - 3 >= 0 and matrix[i][j-1] == 'M' and matrix[i][j-2] == 'A' and matrix[i][j-3] == 'S':
                    count += 1
                    print("Found XMAS at", i, j, "horizontal right-to-left")
                # top-to-bottom
                if i + 3 < len(matrix) and matrix[i+1][j] == 'M' and matrix[i+2][j] == 'A' and matrix[i+3][j] == 'S':
                    count += 1
                    print("Found XMAS at", i, j, "vertical top-to-bottom")
                #bottom-to-top
                if i - 3 >= 0 and matrix[i-1][j] == 'M' and matrix[i-2][j] == 'A' and matrix[i-3][j] == 'S':
                    count += 1
                    print("Found XMAS at", i, j, "vertical bottom-to-top")
                #top-left to bottom-right
                if i + 3 < len(matrix) and j + 3 < len(matrix[i]) and matrix[i+1][j+1] == 'M' and matrix[i+2][j+2] == 'A' and matrix[i+3][j+3] == 'S':
                    count += 1
                    print("Found XMAS at", i, j, "diagonal top-left to bottom-right")
                #top-right to bottom-left
                if i + 3 < len(matrix) and j - 3 >= 0 and matrix[i+1][j-1] == 'M' and matrix[i+2][j-2] == 'A' and matrix[i+3][j-3] == 'S':
                    count += 1
                    print("Found XMAS at", i, j, "diagonal top-right to bottom-left")
                #bottom-left to top-right
                if i - 3 >= 0 and j + 3 < len(matrix[i]) and matrix[i-1][j+1] == 'M' and matrix[i-2][j+2] == 'A' and matrix[i-3][j+3] == 'S':
                    count += 1
                    print("Found XMAS at", i, j, "diagonal bottom-left to top-right")
                #bottom-right to top-left
                if i - 3 >= 0 and j - 3 >= 0 and matrix[i-1][j-1] == 'M' and matrix[i-2][j-2] == 'A' and matrix[i-3][j-3] == 'S':
                    count += 1
                    print("Found XMAS at", i, j, "diagonal bottom-right to top-left")


    print("Total XMAS found:", count)


    input.close()            




if __name__ == "__main__":  
    main()