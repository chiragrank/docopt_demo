# author: Chirag Rank
# date: 2020-11-21

"""This script prints out docopt args.
Usage: docopt.py <arg1> --arg2=<arg2> [--arg3=<arg3>]

Options:
<arg>             Takes any value (this is a required positional argument)
--arg2=<arg2>     Takes any value (this is a required option)
[--arg3=<arg3>]   Takes any value (this is an optional option)
[--arg4=<arg4>]   Takes any value (this is an optional option)
"""

def main():
    print("1")
    print("2")
    print("3")

from docopt import docopt
opt = docopt(__doc__)
print(opt)
print(type(opt))
print(opt["--arg4"])
main()