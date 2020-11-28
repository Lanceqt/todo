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
    created_when: str = str(date.today()) #Must be stringified or tinyDB throws a fit.
    db.insert({"task": task, "status": status, "completed_by": completed_by, "created": created_when})

#reuseable initmenu the type setting is probably not necessary could be like list_todo()
def menu(a: str, r: str, v: str) -> str:
    prompt: str = Prompt.ask(f"please select your destination {a} to Add task, {r} to Remove task, {v} to View Tasks", choices=[a, r, v])
    return prompt

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

#this is where the program starts
print("Welcome user")
init_menu: str = menu("A", "R", "V")

#adds to db.json
if (init_menu == "A"):
    task_name: str = input("Great, please name the task you would like to add!: ")
    task_status: str = "Pending"
    task_complete_by: str = input("When should this task be done by? (example: 30th of december 2020): ")
    try:
        db_insert(task_name, task_status, task_complete_by)
        print("Success! Task has been added.")
    except:
        print("Your task was not added to do an unforeseen error")

#removes from db.json
if (init_menu == "R"):
    init_menu: str = menu("A", "R", "V")

#View db.json   
if (init_menu == "V"):
    list_todo()