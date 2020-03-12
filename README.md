# csvData

## Todo:


- [ ] Scale to really large csv files (2gb maybe?)
- [ ] Get the total number of rows
- [ ] Get the headers for the csv
- [ ] Create a MySQL 'create table' code from the file 
- [ ] Guess the types and lengths (when required) of each column
- [ ] count null or blank values in a col
 
## Assumptions

* CSV file must be openable
* CSV file must contain headers in first row.

## MySQL type guessing

Types to guess:
* int (len)
* datetime
* time
* date
* varchar (len)
* text
* decimal (m,d)