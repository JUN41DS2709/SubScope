from argparse import ArgumentParser
import sys 


parser = ArgumentParser(description="Subscope - A Subdomain Enumerator",
        usage= '%(prog)s  example.com -w wordlist.txt(optional)' ,
        epilog="Example %(prog)s example.com")

parser.add_argument(
    "domain",
    help="domain to scan"
)

parser.add_argument("-v" , 
        help="print version",
        action="version",
        version="%(prog)s v1.0")

parser.add_argument(
    "-w",
    help="Specify wordlist",
    metavar="wordlist",
    dest="wordlist"
)

parser.add_argument("-o",
        help="Save output in a txt file",
        metavar="output",
        dest="output")

args = parser.parse_args()

if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit()
