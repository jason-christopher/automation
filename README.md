# LAB - Class 19

## Project: Automation

### Author: Jason Christopher

### Description

* Given a document potential-contacts, find and collect all email addresses and phone numbers. 
* Phone numbers may be in various formats:
  * (xxx) yyy-zzzz, yyy-zzzz, xxx-yyy-zzzz, etc. 
  * Phone numbers with missing area code should presume 206 
  * Phone numbers should be stored in xxx-yyy-zzzz format. 
* Once emails and phone numbers are found they should be stored in two separate documents.
  * The information should be sorted in ascending order. 
  * Duplicate entries are not allowed.

### Links and Resources

* regex library
* Regex 101

### Setup

To run:

* From the `automation` directory run `python automation.py`.

### Tests

* I used Regex 101 to test the regex strings.
* The given .txt files had exactly 100 valid, non-repeating phone numbers and email addresses. The test would be that the resulting files have exactly 100 valid, non-repeating phone numbers and email addresses. 
