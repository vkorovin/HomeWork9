from modules import data_collection as datasource
class Command():

    def __init__(self,data_source,command,help):
        self.data_source = data_source
        self.command = command
        self.help = help


    def action(self,**params):
        pass

    def  getdescr(self):
        return self.command, self.help


class CommandAdd(Command):
    def action(self, *param):
        self.data_source.add(param[0],param[1])
        print("")


class CommandDone(Command):
    def action(self, *param):
        self.data_source.delete(param[0])


class CommandShow(Command):
    def action(self, *param):
        dataset = self.data_source.get(None,-(param[0]+1),-1)

        print('Title \t\t  Description')
        print('==============================')

        for item in dataset:
            print("{0} \t\t {1}".format(item['title'],item['description']))

if __name__ == '__main__':
    ds = datasource.DataCollection()
    cmd = CommandShow(ds,'show','Show N fresh tasks')

