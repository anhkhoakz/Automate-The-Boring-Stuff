tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    """
    Print table neatly formatted:
    e.g:

    [['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']]

    becomes:

      apples Alice  dogs
     oranges   Bob  cats
    cherries Carol moose
      banana David goose
    """
    # make list of ints to store later max len element of each list
    colWidths = [0] * len(tableData)

    # Store maxlen of each list
    i = 0
    while i < len(tableData):
        colWidths[i] = len(max(tableData[i], key=len))
        i = i + 1

    # Print formatted
    for x in range(len(tableData[0])):
        for y in range(len(colWidths)):
            print(tableData[y][x].rjust(colWidths[y]), end=' ')
        print(end='\n')

printTable(tableData)
