from rich.console import Console
from rich.table import Table
from rich.traceback import install
from rich.prompt import Prompt
from tinydb import TinyDB, Query
install() #better error handling. from rich.traceback

#Database
db = TinyDB('db.json', sort_keys=True, indent=4, separators=(',', ': ')) #for dev
#db = TinyDB('db.json') for "production"

#function to insert into db
def db_insert(task, status, completed_by):
    db.insert({"task": task, "status": status, "completed_by": completed_by})

#init logic & prompt for user entry

init_menu = Prompt.ask("Welcome user please select your destination (A)dd task, (R)emove task, (V)iew Tasks", choices=["A", "R", "V"])


if (init_menu == "A"):
    task_name = input("Great, please name the task you would like to add!: ")
    task_status = "Pending"
    task_complete_by = input("When should this task be done by? (example: 30th of december 2020): ")

    db_insert(task_name, task_status, task_complete_by)

if (init_menu == "R"):
    print("r")
    
if (init_menu == "V"):
    table = Table(title="Todo list")
    table.add_column("Item ID", justify="right", style="green", no_wrap=True)
    table.add_column("Task", style="green")
    table.add_column("Do date", style="green")
    table.add_column("Status", style="green", justify="right")
    console = Console()

    for item in db:
        table.add_row( item["task"], item["completed_by"], item["status"]) #need to find the right command for pulling data out of tinyDB into these example strings

    console.print(table)