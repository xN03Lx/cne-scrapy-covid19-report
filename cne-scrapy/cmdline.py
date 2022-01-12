import sys
from optparse import OptionParser
from utils import get_dni_list


def cmd_parser():
    parser = OptionParser('\n  Cne --dni [DNI,DNI, ...]'
                          '\n  Cne --file [filename]')


    parser.add_option('--dni', type='string', dest='dni', action='store', help='dni set, e.g. 10412244,22370021')
    parser.add_option('--file', '-f', type='string', dest='file', action='store', help='Get dni from txt file.')
    parser.add_option('--output', '-o', type='string', dest='output_dir', action='store', default='./',
                      help='output dir')
    parser.add_option('--name', '-n', type='string', dest='name', action='store', default='dni_data.csv',
                      help='csv file name')

    args, _ = parser.parse_args(sys.argv[1:])

    if args.dni:
        args.dni = get_dni_list(args.dni.split(','))

    if args.file:
        with open(args.file, 'r') as f:
            args.dni = get_dni_list(f.readlines())

    return args
