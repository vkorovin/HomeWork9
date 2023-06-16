from hw9 import data_collection as datasource
from typing import Any, final,  Union, Optional, Callable, Generator, Tuple, List, Dict
import argparse

class Command :

    def __init__(self,data_source: datasource.DataCollection,command:str,descr:str,atype:Dict[str,type]) -> None :
        self.data_source = data_source
        self.command = command
        self.descr = descr
        self.atype = atype


    def action(self, *param: Any ) -> None :
        print(param)

    def  get_descr(self) -> Tuple[str, str, dict[str,type]]:
        return self.command, self.descr, self.atype


@final
class CommandAdd(Command):
     def action(self, *param:Union[str,int]) -> None :
        self.data_source.add(param[0],param[1])
        self.data_source.save()


@final
class CommandDone(Command):
    def action(self, *param:int) -> None :
        self.data_source.delete(len(self.data_source.data) - int(param[0]))
        self.data_source.save()


@final
class CommandShow(Command):
    def action(self, *param:int) -> None :
        dataset = self.data_source.get(None,-(int(param[0])+1),-1)

        print('Index \t\t Title \t\t\t Description')
        print('=========================================================')

        index = 1
        for item in dataset:
            print("{0} \t\t {1} \t\t {2}".format(index,item['title'],item['description']))
            index += 1


@final
class CommandSearch(Command):
    def action(self,*param:Union[str,int]) -> None :
        index_list1 = self.data_source.search('title',param[0])
        index_list2 = self.data_source.search('description', param[0])

        for item in index_list2:
            try:
                index_list1.index(item)
            except:
                index_list1 += (item,)
        print('Found {0} tasks:'.format(len(index_list1)))
        print('Index \t\t Title \t\t\t Description')
        print('=========================================================')

        for item in index_list1[::-1] :
            record = self.data_source.get(item)
            print("{0} \t\t {1} \t\t {2}".format(len(self.data_source.data) - item, record[0]['title'], record[0]['description']))


@final
class CommanndsDict:
    def __init__(self) -> None :
        ds = datasource.DataCollection()
        self.cmddict:dict[str, Command] = dict()

        self.add(CommandAdd(ds, 'add', 'Usage: my-todo add \'title\' \'description\' - Add one task to tasklist',{'tile':str,'description':str}))
        self.add(CommandShow(ds, 'show', 'Usage: my-todo show {n} - Show n freshest task',{'N':int}))
        self.add(CommandDone(ds, 'done', 'Usage: my-todo done {n} - Mark task with index n as cpmpleted and delete it',{'N':int}))
        self.add(CommandSearch(ds, 'search', 'Usage: my-todo search {string} - Search string in title and description and print it',{'sting':str}))

    def add(self, command_class: Command ) -> None :
        cmd,_descr, _atype = command_class.get_descr()
        self.cmddict[cmd] = command_class

    def action(self, cmd:str) -> Callable[[*List[object]], None]:
        return self.cmddict[cmd].action


    def description(self) -> Generator[Tuple[str, str, dict[str,type]], None,None]:
        for item in self.cmddict.values():
             yield item.get_descr()


if __name__ == '__main__':

    cd = CommanndsDict()

    cd.action('show')((1000))
    print(cd.description())
    pass


