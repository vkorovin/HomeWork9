from hw9 import  commands as cmd
import argparse


def run() -> None:
    cmd_dict = cmd.CommanndsDict()

    parser = argparse.ArgumentParser('My-todo console script')
    subcmd = parser.add_subparsers(dest='command', required=True, metavar='command')

    for cmd_name, cmd_descr, cmd_atype  in cmd_dict.description():
        subp = subcmd.add_parser(cmd_name,help = cmd_descr)
        for cmd_arg in cmd_atype:
            subp.add_argument(cmd_arg[0],nargs=1,type=cmd_arg[1])

    args = parser.parse_args()
    cmd_dict.action(args.command)(*args.args)

if __name__ == '__main__':
    run()