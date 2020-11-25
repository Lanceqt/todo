from rich.console import Console
from rich.table import Table
from tinydb import TinyDB, Query

#Database
db = TinyDB('db.json', sort_keys=True, indent=4, separators=(',', ': '))

#Rich table
#todo_list_table = Table()
#todo_list_table.add_column("Todo", style="bold")
#todo_list_table.

db.insert({'type': 'apple', 'count': 7})
db.insert({'type': 'peach', 'count': 3})