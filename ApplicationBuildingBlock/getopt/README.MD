The getopt module is the original command line option parser that supports the conventions established by the Unix function getopt. It parses an argument sequence, such as sys.argv and returns a sequence of tuples containing (option, argument) pairs and a sequence of non-option arguments.

Supported option syntax includes short and long form options:

> -a

>-bval

>-b val

>--noarg

>--witharg=val

>--witharg val

# Function Arguments

The getopt() function takes three arguments:
+ The first parameter is the sequence of arguments to be parsed. This usually comes from sys.argv[1:] (ignoring the program name in sys.arg[0]).

+ The second argument is the option definition string for single character options. If one of the options requires an argument, its letter is followed by a colon.

+ The third argument, if used, should be a sequence of the long-style option names. Long style options can be more than a single character, such as --noarg or --witharg. The option names in the sequence should not include the “--” prefix. If any long option requires an argument, its name should have a suffix of “=”.

Short and long form options can be combined in a single call.

