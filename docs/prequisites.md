# Prerequisites

This document contains an outline of the concepts and techniques that are required for this course. _These concepts will not be taught during the course, and you are expected to have full familiarity with them before starting._

## SQL

* Working with Relational Databases and writing queries to retrieve, manipulate, and filter data from a database.
* `SELECT`, `FROM`, `WHERE` and `ORDER BY` for row and column selection.
* Aggregation via `GROUP BY`
* Join syntax: `LEFT`, `RIGHT`, `INNER` and `OUTER/FULL` joins. 
* String operations: `UPPER`, `LOWER`, `LENGTH`, `TRIM` and how to concatenate two strings.

## Python

* `if-then-else` syntax, `for` loops
* Variable assignment 
* Importing packages
* Comparison operations
* Defining Functions
* Basic Python based data structures and how to manipulate them.
* Strings
  * Slicing using square brackets and colons (e.g. `my_string_var[2:4]`)
  * Replacing subsets of a string using `replace`
  * String functions: `lower`, `upper`, `replace`, `strip`, `index`, `find`/`index`, `len`, `join`, `startswith`.`endswith`and string concatenation 
  * Using `in`
* Lists
  * Creating empty lists and lists from other lists
  * Selecting elements with slice notation
  * Adding items with `append`/`extend`
  * Removing items with `remove`/`pop`
  * Writing list comprehensions with an `if` clause
  * Using `in`
* Dictionaries
  * Creating an empty dictionary or a non-empty dictionary from other variables or atomic/basic data types (literals, primitives, etc. )
  * Adding items
  * Removing items with `pop` or `del`
  * using `.get`
  * `.items`, `.keys` and `.values`
  * Writing dictionary comprehensions with an `if` clause
* Pandas
  * Loading and saving CSV files
  * Selecting rows and columns using `.loc`
  * Using type-specific functions with accessor methods `.str`, `.dt`, etc.
  * Merging with `.merge` 
  * Grouping with `.groupby`