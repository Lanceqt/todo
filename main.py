from rich.console import Console
from rich.table import Table
from rich.traceback import install
from rich.prompt import Prompt
from tinydb import TinyDB, Query
from datetime import date
install() #better error handling. from rich.traceback

#Database
db = TinyDB('db.json', sort_keys=True, indent=4, separators=(',', ': ')) #for dev
#db = TinyDB('db.json') for "production"

#function to insert into db
def db_insert(task: str, status: str, completed_by: str):
    created_when = str(date.today())
    db.insert({"task": task, "status": status, "completed_by": completed_by, "created": created_when})

#reuseable initmenu the type setting is probably not necessary could be like list_todo()
def menu(a: str, r: str, v: str) -> str:
    init_menu = Prompt.ask("Welcome user please select your destination (A)dd task, (R)emove task, (V)iew Tasks", choices=[a, r, v])
    return init_menu

#reuseable listing todo
def list_todo():
    table = Table(title="Todo list")
    table.add_column("Item ID", justify="right", style="green")
    table.add_column("Task", style="green")
    table.add_column("Do date", style="green")
    table.add_column("Status", style="green", justify="right")
    console = Console()

    for item in db:
        table.add_row(str(item.doc_id), item["task"], item["completed_by"], item["status"])
    console.print(table)

init_menu = menu("A", "R", "V")

#adds to db.json
if (init_menu == "A"):
    task_name = input("Great, please name the task you would like to add!: ")
    task_status = "Pending"
    task_complete_by = input("When should this task be done by? (example: 30th of december 2020): ")

    db_insert(task_name, task_status, task_complete_by)

#removes from db.json
if (init_menu == "R"):
    init_menu = menu("A", "R", "V")

#View db.json   
if (init_menu == "V"):
    list_todo()