from hw9 import commands as cmd
import argparse



def convert_args(fake_kwargs:list[tuple[str,object]]) -> list[object]:

    myargs = list()

    for item in fake_kwargs:
        if item[0] == 'command':
            continue
        if type(item[1]) == list and len(item[1]) == 1:
            value, =item[1]
        else:
            value = item[1]
        myargs.append(value)

    return myargs


def run() -> None:
    cmd_dict = cmd.CommanndsDict()

    parser = argparse.ArgumentParser('My-todo console script')
    subcmd = parser.add_subparsers(dest='command', required=True, metavar='command')

    for cmd_name, cmd_descr, cmd_atype  in cmd_dict.description():
        subp = subcmd.add_parser(cmd_name, help = cmd_descr)
        for cmd_arg in cmd_atype.keys():
            subp.add_argument(cmd_arg,nargs=1, type=cmd_atype[cmd_arg])

    args = parser.parse_args()
    fake_kwargs = args._get_kwargs()

    cmd_dict.action(args.command)(*convert_args(fake_kwargs))

if __name__ == '__main__':
    run()