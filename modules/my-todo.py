from modules import  commands
import argparse

def run():
    cmd = commands.CommanndsDict()

    parser = argparse.ArgumentParser(description='My-todo script')

    for cmd_name,cmd_descr in cmd.description():
        parser.add_argument(cmd_name,type=str, help=cmd_descr)
    args = parser.parse_args()
    print(args)
if __name__ == '__main__':
    run()