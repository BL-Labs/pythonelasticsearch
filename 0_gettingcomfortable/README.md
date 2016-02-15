Stage 0: Getting comfortable with the commandline
-------------------------------------------------

In this session, you will be asked to run a number of things ‘from the commandline’ or ‘from a terminal’. If you are not used to doing this, don’t worry! It may seem awkward at first but this part is devoted to making sure everyone is happy running things from it and knowing all you need to know for the rest of the session.

The key theme for running things in a terminal “minimalism”. If you tell it to do something and it succeeds, then 99% of the time, it will say nothing unless you have asked it to. It tells you when something is wrong, not the other way around.

The first thing to get to grips with is that a commandline session is always based somewhere in a filesystem. It has its roots somewhere, and knowing where you are is crucial! 

**pwd** (aka Where am I? literally '*print working directory*')

    [foobar] $ pwd
    /home/(your username)/pythonelasticsearch/0_gettingcomfortable

The '/' at the start of the path is special, and is called the root directory. All *absolute* addresses (or paths) will start with it, and it tells you the full path to that directory on the machine you are using. A path without the '/' at the beginning is a *relative* path. The difference between absolute and relative is the same as the difference between a full postal address and "turn right at the yellow house, go straight on til the big wrought-iron gate". One has meaning everywhere and the other only works as intended if you start in the right place.

Now you know where you are, you'll want to know how to look around: **ls**

	[foobar] $ ls
	*list of the files and subdirectories in the current directory*
	
	[foobar] $ ls some_subdirectory
	*list of the contents of the named subdirectory*
	
	[foobar] $ ls /absolute/path/to/a/directory
	*list the contents of the named directory. This should be the same wherever you are*

Pressing tab to let the machine guess the rest of the path can be very helpful! It's a feature called tab completion and it can save a lot of typing, and it can save you from making typos and other spelling errors!

So, we can find out where we are, and take a look around. How can we move about though? How can we change the directory we are in? 

**cd** (Change Directory) is what is needed. This command can take us from where we are to a new location, if we give it a path. We can give it either an "absolute" (think postal address) or "relative" ("turn left at the lights")

    [foobar] $ ls
    one
    two
    three
    README.md
    [foobar] $ cd one
    [foobar] $

Note how it tells you nothing here. You told it to go into the 'one' directory and it did. If it had an issue, that's when it will report an error. Okay, how can we tell it to go up now? There are two special 'names' to know here. A period "." means "here" and a double period ".." means "up one". For example, following on from above:

	[foobar] $ cd ..
	[foobar] $ ls
	one
	two
	three
	README.md

You may have noticed the 'README.md' file here. Perhaps you would like to read it (or any other text file). You can read it straight away by using another little command 'less'. This isn't particularly logically named application, but it works fine. The only things you need to know is that you can quit it by pressing 'q' and if you press '/' you will be able to search for text within it.

	[foobar] $ less README.md
	*opens a (terminal based) application to let you page through the text, and to search for things*

We cannot discuss finding thing in text and understanding text on the commandline without mentioning two very handy tools called 'grep' and 'wc' (Word Count).

What lines in Ahab.txt have the word Ishmael in?

	[foobar] $ grep Ishmael Ahab.txt 
	Call me Ishmael. Some years ago- never mind how long precisely- having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I... [more text]

How many lines have the word Ishmael in?

	[foobar] $ grep -c 1 Ishmael Ahab.txt

How many words are in 'Ahab.txt'?

	[foobar] $ wc --words Ahab.txt
	2218 Ahab.txt
	[foobar] $ wc --lines Ahab.txt
	34 Ahab.txt

	[foobar] $ wc Ahab.txt
	34  2218 12224 Ahab.txt
	[foobar] $ wc Ahab.txt README.md
	   34  2218 12224 Ahab.txt
	  145  1022  5945 README.md
	  179  3240 18169 total

Finally, a command that we will be using a lot in this session is 'python'. You can use python to run python scripts or, if you run it without a script, it will open a python commandline:

	[foobar] $ python
	Python 3.4.3+ (default, Oct 14 2015, 16:03:50)
	[GCC 5.2.1 20151010] on linux
	Type "help", "copyright", "credits" or "license" for more information.
	>>> _

Now onto a few tasks:

First, go into the directory that corresponds to this section "0_gettingcomfortable". All tasks will start here.

**Task 1:**

What's inside the "one" directory?
Is there anything in there (you may have to keep going deeper)? 
What does it say?

**Task 2:**

Go into "iamadirectory". What happens?

**Task 3:**

How many subdirectories are there in the "0_gettingcomfortable" directory

**Task 4:**

Using 'less':

What is in the Ahab.txt file?
Find the following words by using the search function (press '/' then type in the word)

 - Commodore
 - the
 - horror
 - cataract

How many times do horror and cataract appear?

Now, do the same searching task but use 'grep' instead.


**Task 5:**

Open a python commandline (strictly, this is called an 'interactive session').

Try the following (or similar) commands:

    >>> 2 + 2
    >>> 12039203 * 1232
    >>> 2 ** 8

The following is a glimpse on various things you can do with lists.

    >>> a = ["one", "two", "three", "four"]
    >>> a[0]
    >>> a[-1]
    >>> a.pop(0)
    >>> a(0)
    >>> a[-1]
    >>> a.append("five")
    >>> a[-1]
    >>> a.reverse()
    >>> a
    >>> a.index("one")
    >>> a.index("baaaa")
    >>> b = [1,2,3,4,5]
    >>> a + b

(Don't worry, this task will be explained at the end of this stage.)
