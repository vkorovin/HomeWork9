from hw9 import data_collection as datasource
from typing import final,  Union, Optional


class Command :

    def __init__(self,data_source: datasource.DataCollection, command:str, descr:str) -> None :
        self.data_source = data_source
        self.command = command
        self.descr = descr


    def action(self,*param: Union[int,str] ) -> None :
        print(param)

    def  get_descr(self) -> tuple[str, str] :
        return self.command, self.descr


@final
class CommandAdd(Command):
    def action(self, *param: Union[int,str]) -> None :
        self.data_source.add(param[0],param[1])
        self.data_source.save()


@final
class CommandDone(Command):
    def action(self, *param:Union[int,str]) -> None :
        self.data_source.delete(int(param[0])-1)
        self.data_source.save()


@final
class CommandShow(Command):
    def action(self, *param:Union[int,str]) -> None :
        dataset = self.data_source.get(None,-(int(param[0])+1),-1)

        print('Title \t\t Description')
        print('==============================')

        for item in dataset:
            print("{0} \t\t {1}".format(item['title'],item['description']))


@final
class CommandSearch(Command):
    def action(self,*param:Union[int,str]) -> None :
        index_list1 = self.data_source.search('title',param[0])
        index_list2 = self.data_source.search('description', param[0])

        for item in index_list2:
            try:
                index_list1.index(item)
            except:
                index_list1 += (item,)
        print('Found {0} tasks:'.format(len(index_list1)))
        print('Title \t\t Description')
        print('==============================')

        for item in index_list1:
            record = self.data_source.get(item)
            print("{0} \t\t {1}".format(record[0]['title'], record[0]['description']))


@final
class CommanndsDict:
    def __init__(self) -> None :
        ds = datasource.DataCollection()
        self.cmddict:dict[str, Command] = dict()
        self.add(CommandAdd(ds, 'add', 'Usage: my-todo add \'title\' \'description\' - Add one task to tasklist'))
        self.add(CommandShow(ds, 'show', 'Usage: my-todo show {n} - Show n freshest task'))
        self.add(CommandDone(ds, 'done', 'Usage: my-todo done {n} - Mark task with index n as cpmpleted and delete it'))
        self.add(CommandSearch(ds, 'search', 'Usage: my-todo search {string} - Search string in title and description and print it'))

    def add(self, command_class: Command ) -> None :
        cmd,_descr = command_class.get_descr()
        self.cmddict[cmd] = command_class


    def action(self, cmd:str) :
        return self.cmddict[cmd].action


    def description(self,cmd:Optional[str] = None) -> object :
        if cmd:
            return self.cmddict[cmd].get_descr()
        else:
            for item in self.cmddict.values():
                yield item.get_descr()


if __name__ == '__main__':

    cd = CommanndsDict()

    cd.action('show')(1000)
    print(cd.description('add'))
    pass


