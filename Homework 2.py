
# Name: Rachel Moore
# I worked alone on this assignment.

# PART 1
# 1
import microbit
# microbit.display.set_pixel(0, 0, 9)
# microbit.sleep(200)
# microbit.display.set_pixel(1, 0, 9)
# microbit.sleep(200)
# microbit.display.set_pixel(2, 0, 9)
# microbit.sleep(200)
# microbit.display.set_pixel(3, 0 ,9)
# microbit.sleep(200)
# microbit.display.set_pixel(4, 0, 9)


# 6
def fill_row(time, row):
# function will fill any row one pixel at a time.
# has two paramaters (time and row). time determines how long the row will take to fill, while row indicates which row is being filled.
# no return value.
    microbit.display.set_pixel(0, row, 9)
    microbit.sleep(time // 4)
    microbit.display.set_pixel(1, row, 9)
    microbit.sleep(time // 4)
    microbit.display.set_pixel(2, row, 9)
    microbit.sleep(time // 4)
    microbit.display.set_pixel(3, row ,9)
    microbit.sleep(time // 4)
    microbit.display.set_pixel(4, row, 9)

# fill_row(500, 3)

# 7
def fill_column(time, column):
# function will fill any column one pixel at a time.
# has two paramaters (time and column). time determines how long the column will take to fill, while column indicates which column is being filled.
# no return value.
    microbit.display.set_pixel(column, 0, 9)
    microbit.sleep(time // 4)
    microbit.display.set_pixel(column, 1, 9)
    microbit.sleep(time // 4)
    microbit.display.set_pixel(column, 2, 9)
    microbit.sleep(time // 4)
    microbit.display.set_pixel(column, 3, 9)
    microbit.sleep(time // 4)
    microbit.display.set_pixel(column, 4, 9)

# fill_column(500, 3)

# 1
def fill_by_row(time):
# function will fill the entire microbit row by row.
# has one parameter (time) which depicts how long the entire microbit will take to fill.
# no return value.
    fill_row(time // 5, 0)
    microbit.sleep(time // 25)
    fill_row(time // 5, 1)
    microbit.sleep(time // 25)
    fill_row(time // 5, 2)
    microbit.sleep(time // 25)
    fill_row(time // 5, 3)
    microbit.sleep(time // 25)
    fill_row(time // 5, 4)

# fill_by_row(5000)

#2
def fill_by_column(time):
# function will fill the entire microbit column by column.
# has one parameter (time) which depicts how long the entire microbit will take to fill.
# no return value.
    fill_column(time // 5, 0)
    microbit.sleep(time // 25)
    fill_column(time // 5, 1)
    microbit.sleep(time // 25)
    fill_column(time // 5, 2)
    microbit.sleep(time // 25)
    fill_column(time // 5, 3)
    microbit.sleep(time // 25)
    fill_column(time // 5, 4)

# fill_by_column(10000)

# SIMPLE INTERATION

# 1
def blink(x, y, time):
# function will blink a chosen pixel once.
# has 3 arguments (x, y, time). x is the column while y is the row. Time is the time taken for the pixel to blink.
# no return value.
    microbit.display.set_pixel(x, y, 9)
    microbit.sleep(time)
    microbit.display.set_pixel(x, y, 0)
    microbit.sleep(time)

for i in range(4):
# this is a for loop so that the function blink will repeat four times.
    blink(2, 0, 200)

#1
def fill_row_loop(column, time):
    microbit.display.set_pixel(column, 0, 9)
    microbit.sleep(time // 5)

for i in range(5):
# uses a for loop to fill an entire row.
    fill_row_loop(i, 1000)

#2
def fill_column_loop(row, time):
    microbit.display.set_pixel(0, row, 9)
    microbit.sleep(time // 5)

for i in range(5):
# uses a for loop to fill an entire column.
    fill_column_loop(i, 1000)

#3
def fill_by_row_loop(row):
    fill_row(1000, row)
    microbit.sleep(40)

for i in range(5):
# uses a for loop to fill the entire microbit row by row.
    fill_by_row_loop(i)

# 4

def fill_by_column_loop(i):
    fill_column(1000, i)
    microbit.sleep(40)

for i in range(5):
# uses a for loop to fill the entire microbit column by column.
    fill_by_column_loop(i)