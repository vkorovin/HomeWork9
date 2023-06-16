from pathlib import Path
import json
from typing import final, Optional, Union



@final
class DataStore:


    def __init__(self, path: Optional[str] = None) -> None:
        if not path:
            abspath = Path().absolute()
            self.path = '/' + '/'.join(abspath.parts) + '/todo.store'
        else:
            self.path = path

    def load(self) -> list[Union[str,int]]:

        self.data = list()
        path = Path(self.path)
        if path.is_file():
            with open(path) as json_file:
                self.data = json.load(json_file)

        return self.data

    def save(self, data: Optional[list[str]] = None) -> None:

        with open(self.path, 'w') as json_file:
            if data:
                json.dump(data, json_file)
            else:
                json.dump(self.data, json_file)


if __name__ == '__main__':
    ds = DataStore()
    data = [
        {'title': 'MyTitle0', 'description': 'MyDescription1', 'deleted': False},
        {'title': 'MyTitle1', 'description': 'MyDescription2', 'deleted': False},
        {'title': 'MyTitle2', 'description': 'MyDescription3', 'deleted': False},
    ]
    #ds.save(data)
    print(ds.load())
