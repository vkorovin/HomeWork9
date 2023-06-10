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




if __name__ == '__main__':
    ds = datasource.DataCollection()
    cmd = CommandSearch(ds,'show','Show N fresh tasks')
    cmd.action('Title')

