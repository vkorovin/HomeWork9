from modules import  commands as cmd
import argparse

def run():
    cmd_dict = cmd.CommanndsDict()

    parser = argparse.ArgumentParser('My-todo console script')
    subcmd = parser.add_subparsers(dest='command', required=True, metavar='command')

    for cmd_name, cmd_descr in cmd_dict.description():
        subp = subcmd.add_parser(cmd_name,help = cmd_descr)
        subp.add_argument('args',nargs='*')

    args = parser.parse_args()
    cmd_dict.action(args.command)(*args.args)

if __name__ == '__main__':
    run()