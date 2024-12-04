

# We are given a search input where any letters that are not X M A S are irrelevant.
# within those letters that are left we have to find the word "XMAS" which could be horizontal, vertical, diagonal, written backwards, or even overlapping other words.
# We have to find all of them and count


# TASK 2 --> find all of the cross shaped M A S and coutn them

def main():
    input = open("input.txt", "r")

    # read the input as a matrix of characters where num of columns = input line length

    line = input.readline().strip()
    
    matrix = []
    while line:
        matrix.append(list(line))
        line = input.readline().strip()

    # for i in range(len(matrix)):
    #     print(matrix[i])

    # print()

    # search for XMAS in all directions
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'X':
                #left-to-right
                if j + 3 < len(matrix[i]) and matrix[i][j+1] == 'M' and matrix[i][j+2] == 'A' and matrix[i][j+3] == 'S':
                    count += 1
                # right-to-left
                if j - 3 >= 0 and matrix[i][j-1] == 'M' and matrix[i][j-2] == 'A' and matrix[i][j-3] == 'S':
                    count += 1
                # top-to-bottom
                if i + 3 < len(matrix) and matrix[i+1][j] == 'M' and matrix[i+2][j] == 'A' and matrix[i+3][j] == 'S':
                    count += 1
                #bottom-to-top
                if i - 3 >= 0 and matrix[i-1][j] == 'M' and matrix[i-2][j] == 'A' and matrix[i-3][j] == 'S':
                    count += 1
                #top-left to bottom-right
                if i + 3 < len(matrix) and j + 3 < len(matrix[i]) and matrix[i+1][j+1] == 'M' and matrix[i+2][j+2] == 'A' and matrix[i+3][j+3] == 'S':
                    count += 1
                #top-right to bottom-left
                if i + 3 < len(matrix) and j - 3 >= 0 and matrix[i+1][j-1] == 'M' and matrix[i+2][j-2] == 'A' and matrix[i+3][j-3] == 'S':
                    count += 1
                #bottom-left to top-right
                if i - 3 >= 0 and j + 3 < len(matrix[i]) and matrix[i-1][j+1] == 'M' and matrix[i-2][j+2] == 'A' and matrix[i-3][j+3] == 'S':
                    count += 1
                #bottom-right to top-left
                if i - 3 >= 0 and j - 3 >= 0 and matrix[i-1][j-1] == 'M' and matrix[i-2][j-2] == 'A' and matrix[i-3][j-3] == 'S':
                    count += 1


    print("Total XMAS found:", count)


    # TAKS 2

    count_MAS = 0

    # search for MAS in all diagonals
    dircetions = [
        (1,1), #down-right
        (1,-1), #down-left
        (-1,1), #up-right
        (-1,-1) #up-left
    ]
    
    for i in range(len(matrix)):
        print(matrix[i])
    
    word = "MAS"
    centers = []
 
    # check for MAS in all diagonals and save their centers
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for dir_x, dir_y in dircetions:
                found = True
                for k in range(3):
                    x = i + k * dir_x
                    y = j + k * dir_y
                    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[i]) or matrix[x][y] != word[k]:
                        found = False
                        break
                if found:
                    center_x = i + dir_x  
                    center_y = j + dir_y 
                    print(f"Found MAS at: ({i}, {j}), Direction: ({dir_x}, {dir_y}), Center: ({center_x}, {center_y})")
                    centers.append((center_x, center_y))

    # find those that share center and count them
    for i in range(len(centers)):
        for j in range(i+1, len(centers)):
            if centers[i] == centers[j]:
                count_MAS += 1


    print("Total X-MAS found:", count_MAS)
    input.close()            


if __name__ == "__main__":  
    main()