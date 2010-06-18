# Summary
Lython is a new lisp front-end for the Python programming language.
It resembles common lisp and compiles directly to Python bytecodes and 
transparently integrates with existing Python code and libraries.

It currently provides a very limited macro system.  It is hoped that
it will one day support full-blown lisp procedural macros.

# Limitations
This is a very early proof of concept release and is in no way ready
for real production use.

# Installation
Just unpack the source and run the lython executable.  If you relocate the
lython executable you must make sure that the spark.py library is on Python's
load path.

Try running ./lython tests/operators for a start.

# Acknowledgements
Lython depends heavily on the John Aycock's excellent 
[spark parser toolkit](http://pages.cpsc.ucalgary.ca/~aycock/spark)




