from rich.console import Console
from rich.table import Table
from rich.traceback import install
from rich.prompt import Prompt
from tinydb import TinyDB, Query
from datetime import date
install() #better error handling. from rich.traceback

#Database
DB = TinyDB('db.json', sort_keys=True, indent=4, separators=(',', ': ')) #for dev
#db = TinyDB('db.json') for "production"

#function to insert into db
def db_insert(task: str, status: str, completed_by: str):
    created_when: str = str(date.today()) #Must be stringified or tinyDB throws a fit.
    DB.insert({"task": task, "status": status, "completed_by": completed_by, "created": created_when})

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
    
    for item in sorted(DB, key = lambda i: int(i.doc_id)): #Lambda is like an inline function see below it's the same putting this here for my own reference and learning.
    #def foo(i):
    #   return int(i.doc_id)
    #   for item in sorted(db, key = foo):
        table.add_row(str(item.doc_id), item["task"], item["completed_by"], item["status"])

    console.print(table)

#this is the main program
def main(user_message: str):
    #this is how we exit the loop call exit_program("message", "affirmative", "negative") after task with
    def exit_program(m: str, y: str, n: str) -> bool:
        exit_prompt: str = Prompt.ask(f"{m}", choices=[y, n])
        if (exit_prompt == y):
            return False
        else:
            return True

    print(user_message)
    run_program: bool = True

    while (run_program == True):
        init_menu: str = menu("A", "R", "V")

        #adds to db.json
        if (init_menu == "A"):
            task_name: str = input("Great, please name the task you would like to add!: ")
            task_status: str = "Pending"
            task_complete_by: str = input("When should this task be done by? (example: 30th of december 2020): ")
            try:
                db_insert(task_name, task_status, task_complete_by)
                run_program = exit_program("Success! Task has been added. Exit?", "Yes", "No")
            except:
                print("Your task was not added to do an unforeseen error")

        #removes from db.json
        if (init_menu == "R"):
            run_program: bool = exit_program("Success! Task have ben removed. Exit?", "Yes", "No")
        #View db.json   
        if (init_menu == "V"):
            list_todo()
            run_program: bool = exit_program("Wanna exit the program?", "Yes", "No")

#running program
if __name__ == '__main__': 
    main("Welcome user")
else:
    print("this file is not suppose to be imported anywhere you done goofed")