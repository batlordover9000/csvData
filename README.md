# csvData


## Usage:
- clone repo
- rename config.sample.py to config.py
- change DB credential in config.py
- python3 csvData.py mycsvfile.csv


## Todo:


- [x] Scale to really large csv files (2gb maybe?)
- [x] Get the total number of rows
- [x] Get the headers for the csv
- [x] Create a MySQL 'create table' code from the file 
- [x] Guess the types and lengths (when required) of each column
- [ ] count null or blank values in a col
 
## Assumptions

* CSV file must be openable
* CSV file must contain headers in first row.

## MySQL type guessing

Types to guess:
* datetime
* date
* decimal (m,d)
* int (len)
* varchar (len)


Process for type guessing:
* iterate over columns
	* iterate over all rows for one col
		* Create tally of votes for each type
		* count the number of special chars:
			* what are these counts?
