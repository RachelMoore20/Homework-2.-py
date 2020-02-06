
# Name: Rachel Moore
# I worked alone on this assignment.

# CHAPTER 3 EXERCISE 3

grid_2 = [1,2,2,2,2,1,2,2,2,2,1]
# grid_2 serves as a list of numbers that will later be assigned patterns in an order that forms a grid with 3 rows and 3 columns.

for pattern in grid_2:
    if pattern == 1:
        print('+ - - - - + - - - - +')
# this assigns the value 1 a pattern so that every time 1 appears in the list, the pattern will appear.
        continue
    if pattern == 2:
        print('/         /         /')
# this assigns the value 2 a pattern so that every time 2 appears in the list, the pattern will appear.
        continue
    print(pattern)
# this prints the list with the assigned patterns to replace 1 and 2. Forms grid.


grid_4 = [1,2,2,2,2,1,2,2,2,2,1,2,2,2,2,1]
# grid_4 serves as a list of numbers that will later be assigned patterns in an order that forms a grid with 4 rows and 4 columns.

for pattern in grid_4:
    if pattern == 1:
        print('+ - - - - + - - - - + - - - - +')
# this assigns the value 1 a pattern so that every time 1 appears in the list, the pattern will appear.
        continue
    if pattern == 2:
        print('/         /         /         /')
# this assigns the value 2 a pattern so that every time 2 appears in the list, the pattern will appear.
        continue
    print(pattern)
# this prints the list with the assigned patterns to replace 1 and 2. Forms grid.



