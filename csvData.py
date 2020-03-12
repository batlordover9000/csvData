import os,csv,re

class csvData:
    
    def __init__(self,fn):
        canopen = False
        try:
            f = open(fn,'r')
            f.close()
            canopen = True
        except Exception as e:
            print('Could not open ' , fn)
        self.canopen = canopen
        if self.canopen:
            self.filename = fn
            #self.filepath = ''
            self.col_delimiter = ','
            self.row_delimiter = '\n'
            self.totalRows = 0
            self.originalFields = []
            self.filteredFields = []
            self.mismatchRows = []
            self.f = None
            self.getFields()
    def getReader(self):
        self.f = open(self.filename,"r",newline=self.row_delimiter)
        reader = csv.reader(self.f,delimiter=self.col_delimiter)
        return reader
    def getFields(self):
        n=0
        reader = self.getReader()
        for row in reader:
            self.originalFields = row
            break
        self.f.close()
        self.filteredFields = []
        for field in self.originalFields:
            s = field.lower().strip()
            s = s.replace(' ','_')
            s = re.sub(r'[^0-9a-z_]', '', s)
            #print(field, s)
            self.filteredFields.append(s)
    def checkShape(self):
        reader = self.getReader()
        #get the total number of cols
        #get the total number of rows
        #indicate whether any rows have a dif # of cols
        rows = 0
        mr = []
        self.mismatchRows = []
        for row in reader:
            if len(self.originalFields) != len(row):
                mr.append(rows)
            rows+=1
        self.f.close()
        self.totalRows = rows
        self.mismatchRows = mr        