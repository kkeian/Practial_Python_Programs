grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# this determines the length of the first nested list
#  it uses this integer value as the input for the range
#  function.
#
#  (the [0, 0] origin is at the first item of the first list

for i in range(len(grid[0])):
    # this looks at the 'grid' list variable with each
    #  nested list viewed as one item. 'n' is the counter
    #  that is used to keep track of how many iterations
    #  have been done. 
    #
    #  this is keeping track of the 'y' value used in the
    #  coordinate scheme.
    #
    #  the program uses 'i' as the 'x' value and 'n' as the
    #  'y' value. it determines that i = 0 at the first run
    #  then it determines that in the nested loop, n = 0
    #  it maintains that i = 0 for each iteration through
    #  the nested loop, and increments n by 1, each time
    #  it repeats the loop. the "end=''" part inside
    #  the print() function tells print, to not use it's
    #  default, which is the
    #  newline character it outputs after it determines 
    #  the result of the function's input.
    #
    #  after the program finishes iterating through the
    #  first item in each nested list, it breaks out of the
    #  nested loop and increments the 'i' counter by 1.
    #  it then returns to the nested loop and performs the
    #  nested loop iteration as detailed in the
    #  preceding paragraph.
    #
    # NOTE: the "end=''" keyword argument in the print
    #  statement that is inside the nested "for" loop
    #  does not apply to the parent "for" loop. as such,
    #  a "newline" character IS printed after the nested
    #  loop, breaks.
    
    for n in range(len(grid)):
        print(grid[n][i], end='')
# This print() function is indented so that it is performed
#  immediately after the nested loop finishes, and before
#  the parent loop increments.
    print()

# Solution by: kilocatt via github.com https://stackoverflow.com/questions/30424355/automate-the-boring-stuff-with-python-chapter-4-exercise
