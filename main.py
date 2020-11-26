from rich.console import Console
from rich.table import Table
from rich.traceback import install
from tinydb import TinyDB, Query
install() #better error handling. from rich.traceback

#Database
db = TinyDB('db.json', sort_keys=True, indent=4, separators=(',', ': ')) #for dev
#db = TinyDB('db.json') for "production"

#Rich table
#todo_list_table = Table()
#todo_list_table.add_column("Todo", style="bold")
#todo_list_table.

#function to insert into db
def insert(task, status, completed_by):
    db.insert({"task": task, "status": status, "completed_by": completed_by})

