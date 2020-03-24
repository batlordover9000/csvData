from csvData import csvData

c = csvData('sample2.csv')
if c.canopen:
    print(c.filename)
    print(c.originalFields)
    print(c.filteredFields)
    c.guessTypes()
    #c.checkShape()
#c.loadFile('sample.csv')

