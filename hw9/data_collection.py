from hw9 import ds
import re
from typing import final, Optional, Union


DataSet = list[dict[ str, str]]


@final
class DataCollection:
    def __init__(self) -> None:
        self.datastore=ds.DataStore()
        self.data=self.datastore.load()


    def add(self, title: Union[int,str], description:Union[int,str]) -> None :
        self.data.append({'title':title,'description':description})


    def delete(self, index:int) -> None :
        self.data.pop(index)


    def get(self,start:Optional[int]=None, stop:Optional[int]=None,step:Optional[int]=None) -> DataSet:
        return self.data[start:stop:step]


    def search(self,field:Union[int,str], value:Union[int,str]) -> tuple[int, ...] :
        index = 0
        found: tuple[int, ...] =()
        for item in self.data:
            if re.search(value,item[field]):
                found += (index,)
            index += 1
        return found

    def save(self) -> None:
        self.datastore.save()


if __name__ == '__main__':
    dc = DataCollection()

    dc.add('MyTitle0', 'MyDescription0')
    dc.add('MyTitle1', 'MyDescription1')
    dc.add('MyTitle2', 'MyDescription2')
    dc.add('MyTitle3', 'MyDescription3')
    dc.add('MyTitle4', 'MyDescription4')

    print(dc.get())
    dc.save()

    print(dc.get())









