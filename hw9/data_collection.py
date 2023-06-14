from hw8 import ds
import re


class DataCollection():
    def __init__(self):
        self.datastore=ds.DataStore()
        self.data=self.datastore.load()


    def add(self, title,description):
        self.data.append({'title':title,'description':description})


    def delete(self,index):
        self.data.pop(index)


    def get(self,start=None,stop=None,step=None):
        return self.data[start:stop:step]


    def search(self,field,value):
        index = 0
        found =()
        for item in self.data:
            if re.search(value,item[field]):
                found += (index,)
            index += 1
        return found
    def save(self):
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









