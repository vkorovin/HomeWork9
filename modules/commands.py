from modules import data_collection as datasource
class Command():

    def __init__(self,data_source,command,help):
        self.data_source = data_source
        self.command = command
        self.help = help


    def action(self,*param):
        print(param)

    def  get_descr(self):
        return self.command, self.help


class CommandAdd(Command):
    def action(self, *param):
        self.data_source.add(param[0],param[1])
        self.data_source.save()


class CommandDone(Command):
    def action(self, *param):
        self.data_source.delete(param[0])
        self.data_source.save()

class CommandShow(Command):
    def action(self, *param):
        dataset = self.data_source.get(None,-(param[0]+1),-1)

        print('Title \t\t  Description')
        print('==============================')

        for item in dataset:
            print("{0} \t\t {1}".format(item['title'],item['description']))


class CommandSearch(Command):
    def action(self,*param):
        index_list1 = self.data_source.search('title',param[0])
        index_list2 = self.data_source.search('description', param[0])

        for item in index_list2:
            try:
                index_list1.index(item)
            except:
                index_list1 += (item,)
        print('Found {0} tasks:'.format(len(index_list1)))
        print('Title \t\t\t Description')
        print('==============================')

        for item in index_list1:
            record = self.data_source.get(item)
            print("{0} \t\t {1}".format(record[0]['title'], record[0]['description']))

class CommanndsDict():
    def __init__(self):
        ds = datasource.DataCollection()
        self.cmddict = dict()
        self.add(CommandAdd(ds, 'add', 'Usage: my-todo add \'title\' \'description\' - Add one task to tasklist'))
        self.add(CommandShow(ds, 'show', 'Usage: my-todo show {n} - Show n freshest task'))
        self.add(CommandDone(ds, 'done', 'Usage: my-todo done {n} - Mark task with index n as cpmpleted and delete it'))
        self.add(CommandSearch(ds, 'done', 'Usage: my-todo search {string} - Search string in title and description and print it'))

    def add(self, command_class ):
        cmd,_descr = command_class.get_descr()
        self.cmddict[cmd] = command_class

    def action(self,cmd):
        return self.cmddict[cmd].action
    def description(self,cmd):
        return self.cmddict[cmd].get_descr()


if __name__ == '__main__':

    cd = CommanndsDict()

    cd.action('show')(1000)
    print(cd.description('add'))
    pass


