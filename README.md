# csvData

## Todo:


- [x] Scale to really large csv files (2gb maybe?)
- [x] Get the total number of rows
- [x] Get the headers for the csv
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
* date
* varchar (len)
* decimal (m,d)

Process for type guessing:
* iterate over columns
	* iterate over all rows for one col
		* Create tally of votes for each type
		* count the number of special chars:
			* what are these counts?