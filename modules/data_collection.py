from modules import ds
import re
class DataCollection():
    """
    Primitives of data collection operations. Every data items have 'deleted' attribute
    to mark deleted record. Physical records deletes on  data save only.
    """
    def __init__(self):
        self.datastore=ds.DataStore()
        self.data=self.datastore.load()

    def add(self, title,description):
        self.data.append({'title':title,'description':description, 'deleted':False})

    def delete(self,index):
        try:
            self.data[index]['deleted'] = True
        except IndexError:
            pass

    def show(self,start=None,stop=None,step=None):
        return self.data[start:stop:step]

    def select(self, index= -1, count=1):
        if(index < 0):
            count = len(self.data)
        pos = 0
        while  pos < count:
            pos += 1
            try:
                if not self.data[index+pos-1]['deleted']:
                    yield self.data[index+pos-1]
                else:
                    pos -= 1
            except IndexError:
                pos = count
    def pack(self):
        index =0
        for item in self.data:
            if item['deleted'] :
                self.data.pop(index)
            index += 1

    def search(self,field,value):
        index = 0
        found =()
        for item in self.data:
            if re.search(value,item[field]) and not item['deleted']:
                found += (index,)
            index += 1
        return found

    def save(self):
        self.pack()
        self.datastore.save()

if __name__ == '__main__':
    dc = DataCollection()
    dc.add('MyTitle0', 'MyDescription1')
    dc.add('MyTitle0', 'MyDescription1')
    dc.add('MyTitle0', 'MyDescription1')
    dc.add('MyTitle0', 'MyDescription1')
    dc.add('MyTitle0', 'MyDescription1')

    print(len(dc.data))
    strings = dc.show()
    print(strings)
    dc.save()
    #dc.delete(1)


    #dc.save()
    #print(dc.data)



