from pathlib import Path
import json

class DataStore():
    """
    Only dirty operation in this class (save and load JSON file)
    """
    def __init__(self,path=None):
        if not path: # if path not defined store date in ../data/todo.store
            abspath =  Path().absolute()
            self.path = '/'+'/'.join(abspath.parts) + '/todo.store'
        else:
            self.path = path

    def load(self):
        path = Path(self.path)
        if path.is_file():
            with open(path) as json_file:
                self.data = json.load(json_file)
        else:
                self.data = list()

        return self.data
    def save(self,data=None):
        with open(self.path, 'w') as json_file:
            if data:
                 json.dump(data,json_file)
            else:
                 json.dump(self.data, json_file)


if __name__ == '__main__':
    ds = DataStore()
    data = [
                    {'title':'MyTitle0','description':'MyDescription1', 'deleted':False},
                    {'title': 'MyTitle1', 'description': 'MyDescription2', 'deleted': False},
                    {'title': 'MyTitle2', 'description': 'MyDescription3', 'deleted': False},
      ]
    ds.save(data)