Stage 1: Basics of dealing with CSVs and data structures in python
-------------------------------------------------

This stage will explain more about handling CSVs, specifically in python, but it is not intended to teach you how to program. We're going to go through some basic terms and get a workable understanding for what CSVs and how python holds data, and also of how the code precedes with making it useful for us.

CSV stands for Comma-Separated Values. (TSV is intimately related, Tab-Separated Values but we'll focus on CSV for the time being.) It is a standard for representing a table of data in a single 'human readable' file. It may not be intelligible, but you should be able to at least understand what it concerns with very basic text tools.

**One CSV will represent one table of data and little else.** It is like a spreadsheet but doesn't encapsulate anything about formatting, display, formulas, cell references and so on. It is a text file, where each line corresponds to a single row of data, and each header or value in the row is separated by a comma. They are quick to read and quick to create, and allow you to work on them row-by-row, so excellent for holding data in intermediate (and often, final) stages of data processing. The standard doesn't consider how to help people reading the CSV to better understand the content though! 

One key piece of the CSV is the first line. This holds the column 'headers' and is a way for authors to indicate what each column means. How can we see this? **head** is a great tool for this:

	[foobar] $ head data/bibliographic.csv
	sysnum,title,author,date,place
	(and 9 other lines too.)
	[foobar] $ 

The command **head**, like almost all terminal commands, can act differently if we tell it to. We can tell it to only return the first line using the 'flag' "-n 1":

	[foobar] $ head -n 1 data/bibliographic.csv
	sysnum,title,author,date,place
	[foobar] $ 

This is a handy trick, especially for huge CSV (and TSV) files as other applications will often try to load the entire file first, whereas **head** just does what you tell it to. If the file is comparatively large (>2GB), this is likely a good first step. (It works on many text-based files too, like XML.)

Stage 1: Basics of dealing with CSVs and "JSON-like" data in python
-------------------------------------------------

This stage will explain more about handling CSVs, specifically in python, but it is not intended to teach you how to program. We're going to go through some basic terms and get a workable understanding for what CSVs and JSON are, and also of how the code precedes with making it useful for us.

CSV stands for Comma-Separated Values. (TSV is intimately related, Tab-Separated Values but we'll focus on CSV for the time being.) It is a standard for representing a table of data in a single 'human readable' file. It may not be intelligible, but you should be able to at least understand what it concerns with very basic text tools.

**One CSV will represent one table of data and little else.** It is like a spreadsheet but doesn't encapsulate anything about formatting, display, formulas, cell references and so on. It is a text file, where each line corresponds to a single row of data, and each header or value in the row is separated by a comma. They are quick to read and quick to create, and allow you to work on them row-by-row, so excellent for holding data in intermediate (and often, final) stages of data processing. The standard doesn't consider how to help people reading the CSV to better understand the content though! 

One key piece of the CSV is the first line. This holds the column 'headers' and is a way for authors to indicate what each column means. How can we see this? **head** is a great tool for this. Move into the "1_csv" folder from the start of the course directory and try the following:

	[foobar] $ head broken_data.csv
	sysnum,title,author,date,place
	(and 9 other lines too.)
	[foobar] $ 

The command **head**, like almost all terminal commands, can act differently if we tell it to. We can tell it to only return the first line using the 'flag' "-n 1":

	[foobar] $ head -n 1 broken_data.csv
	sysnum,title,author,date,place
	[foobar] $ 

This is a handy trick, especially for huge CSV (and TSV) files as other applications will often try to load the entire file first, whereas **head** just does what you tell it to. If the file is comparatively large (>2GB), this is likely a good first step. (It works on many text-based files too, like XML.)

Let's open a CSV in python and explore how to work with it. First thing we have to do is open a python interactive session and 'import' the module that makes dealing with CSVs very easy.

	[foobar] $ python
	>>> import csv

Now that we've loaded in some code that will handle the CSV format for us, let's open some data to explore:

	>>> datafile = open("broken_data.csv")
	>>> data = csv.reader(datafile)

This has opened the file called "broken_data.csv" and created an object that can understand the CSV format and that has been assigned that file to work on. No data has been loaded, and none of the CSV has actually been looked at yet! The csv module lets you work with a CSV on a line-by-line basis, as if it were a big list of data rows. We can use a '\__next\__' method to examine the 'next' line without working through the whole file. 

	>>> data.line_num
	0
	>>> headers = data.__next__()
	>>> data.line_num
	1
	>>> headers
	['sysnum', 'title', 'author', 'date', 'place']

These are the CSV headers, shown in the order that they appear in the file. The first column is the 'sysnum' which is one of the identifiers that the library uses within the main library catalogue. Like this session, counting in python (and many other languages) begins at zero.

	>>> headers[0]
	'sysnum'
	>>> headers[4]
	'place'
	>>> headers[100]
	?... (try this!)
	>>> headers[-1]
	?... (try this!)

Now, let's look at some real data:

	>>> first = data.__next__()
	>>> first
	['001316031', 'Curabitur in libero ut massa volutpat convallis. Morbi odio odio, elementum eu, interdum eu, tincidunt in, leo. Maecenas pulvinar lobortis est.', '', '1896', 'Kjøbenhavn']

Great! But there is something wrong! Nothing wrong with what we are doing, but the data itself is wrong! No wonder it is called 'broken_data.csv'!

We'll get back to this later, but first, we'll write some code to go through all the lines BUT only write the place the book was published in. Note that the following is incomplete. You need to replace the * with a number that corresponds to the correct column:

	>>> for row in data:
	...   print(row[*])

Run the "for row in ..." lines for a second time. What happened?

There is a "csv.writer", which allows you write out rows of data in a CSV format, just by opening a file for writing, and writing rows of data to it:

	>>> # the "w" tells the open command to
	>>> # open the file for writing
	>>> f = open("random_file.csv", "w")
	>>> w = csv.writer(f)
	>>> w.writerow(["title", "author", "date", "identifier"])
	>>> w.writerow(["Tank", "Spike", "2340", "Bebop"])
	>>> f.close() # this closes the file, flushing it to storage

There is another way to use the csv module to read and write CSV files and that is "csv.DictReader" and "csv.DictWriter". Rather than use the headers ourselves, we can let the module handle that part. We don't need to work out what number column which sort of data is in, we can just call it by name.

	>>> f = open("broken_data.csv")
	>>> d_reader = csv.DictReader(f)
	>>> row = d_reader.__next__()
	>>> row
	{'title': 'Curabitur in libero ut massa volutpat convallis. Morbi odio odio, elementum eu, interdum eu, tincidunt in, leo. Maecenas pulvinar lobortis est.', 'sysnum': '001316031', 'place': 'Kjøbenhavn', 'date': '1896', 'author': ''}
	>>> row['place']
	'Kjøbenhavn'

csv.DictWriter works in a similar way, but you should define what the csv headers are when you create it:

	>>> f = open("random_file.csv", "w")
	>>> d_writer = csv.DictWriter(f, fieldnames=["title", "author", "date", "identifier"])
	>>> # You still need to write a row out for the headers:
	>>> d_writer.writerow({"title": "title", "author":"author", "date":"date", "identifier":"identifier"})
	>>> d_writer.writerow({'title':'Tank', 'author': "Spike", ... etc })
	>>> f.close()

Now it's time to fix that file! There is a second csv which just has two columns - the sysnum, and the correct title for that book. How to combine them? Time to look at some code!

Aim: 

1. Create a way to look up the correct title, given the system number of the book.
2. Run through the broken CSV, replacing the spurious titles with the correct ones.
3. Create a third CSV, which has the correct information. 

*Most* of the code to do this has been written for you. It doesn't work however!

**Task 1:**

First, make sure you can edit and run code! Create a new file in your text editor, and write code to open and print all of the "patch_data.csv". This will be nearly identical to the example this stage ran through at the beginning, but we will be examining a different CSV file.

Hint: You need to "import csv", open the file, create a csv.reader of it and then use the "for row in ..." lines to print it out again.

**Task 2:**

Try running the following command:

	[foobar] $ python patch.py

It fails! Open patch.py in a text editor and try to fix the two errors in the file. Run the command again when you think you have fixed it, and it will tell you when it works correctly!

Hints: The deliberate errors introduced are representative of the most commons problems people have running code. Check that you have all the files the code needs, that files and headers are named correctly, and that the data looks like you think it should.

**Task 3:**

Much like above, but with "fix_data.py":

	[foobar] $ python fix_data.py

Again, the errors are similar to common ones that you will likely encounter in real life.

**Task 4:**

By the end of the third task, you should have a new, third file in the directory called "fixed_data.csv". Make sure that it looks as you anticipated.

**Task 5:**

Look at the file called "Bad_but_perfectly_legal.csv". Try to open it in a text editor and less.


**Finally**

This stage will finish with a small note about what to watch out for when working with Excel and CSVs, and about how text data is stored. (An entire session could be devoted to the issues you might encounter!)
