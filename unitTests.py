from csvData import csvData

c = csvData('sample.csv')
if c.canopen:
    print(c.filename)
    print(c.originalFields)
    print(c.filteredFields)
    c.checkShape()
#c.loadFile('sample.csv')

