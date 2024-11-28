import argparse
from typing import List, Optional, Union, Any, Tuple
from colorama import Fore, Style, init
from enums import Action, Status
from storage.json_handler import JsonHandler
from tasks import TaskManager

# Initialize Colorama
init(autoreset=True)

parser = argparse.ArgumentParser()
parser.add_argument(
    "action",
    choices=[action.value for action in Action],
    help="The action to perform (add, delete, update, list)",
)
parser.add_argument(
    "params",
    nargs="*",
    help="Additional parameters for the action (e.g., task ID, description)",
)
args = parser.parse_args()

storage: JsonHandler = JsonHandler()
task_manager: TaskManager = TaskManager(storage)

def main() -> str | list[Any] | tuple[str, dict]:
    if args.action == Action.ADD:
        if len(args.params) != 1:
            return f"{Fore.RED}Error: The 'add' action requires exactly one argument: the description.{Style.RESET_ALL}"
        else:
            description: str = args.params[0]
            if task_manager.check_availability(description):
                return f"{Fore.YELLOW}Task already added{Style.RESET_ALL}"
            else:
                task = task_manager.add_task(description)
                return f"{Fore.GREEN}Task added successfully (ID: {task.id}){Style.RESET_ALL}"
    elif args.action == Action.UPDATE:
        if len(args.params) != 2:
            return f"{Fore.RED}Error: The 'update' action requires two arguments: ID and description.{Style.RESET_ALL}"
        else:
            task_id: str
            description: str
            task_id, description = args.params
            try:
                task_id_int: int = int(task_id)
                if task_manager.check_availability(task_id=task_id_int):
                    if task_manager.check_exact(task_id=task_id_int, description=description):
                        return f"{Fore.YELLOW}Task is up to date{Style.RESET_ALL}"
                    else:
                        task_manager.update_description(task_id_int, description)
                        return f"{Fore.GREEN}Task with ID {task_id_int} updated to '{description}'.{Style.RESET_ALL}"
                return f"{Fore.RED}Task doesn't exist{Style.RESET_ALL}"
            except ValueError:
                return f"{Fore.RED}Error: The task ID must be an integer.{Style.RESET_ALL}"
    elif args.action == Action.DELETE:
        if len(args.params) != 1:
            return f"{Fore.RED}Error: The 'delete' action requires exactly one argument: the ID.{Style.RESET_ALL}"
        else:
            try:
                task_id: int = int(args.params[0])
                if task_manager.check_availability(task_id=task_id):
                    task_manager.delete_task(task_id)
                    return f"{Fore.GREEN}Task with ID {task_id} deleted.{Style.RESET_ALL}"
                else:
                    return f"{Fore.RED}Task doesn't exist{Style.RESET_ALL}"
            except ValueError:
                return f"{Fore.RED}Error: The task ID must be an integer.{Style.RESET_ALL}"
    elif args.action == Action.LIST:
        if len(args.params) not in (0, 1):
            return f"{Fore.RED}Error: The 'list' action requires exactly one argument to filter tasks: the task status.{Style.RESET_ALL}"
        tasks: dict = task_manager.list_tasks()
        if args.params:
            status: str = args.params[0]
            if not tasks:
                return f"{Fore.YELLOW}Tasks aren't exist{Style.RESET_ALL}"
            return [tasks[task] for task in tasks if tasks[task]['status'] == status]
        else:
            return f"{Fore.GREEN}Tasks:{Style.RESET_ALL}", tasks
    elif args.action in (Action.MARK_IN_PROGRESS, Action.MARK_DONE):
        status: Status = Status.IN_PROGRESS if args.action == Action.MARK_IN_PROGRESS else Status.DONE
        if len(args.params) != 1:
            return f"{Fore.RED}Error: This action requires ID.{Style.RESET_ALL}"
        task_id: str = args.params[0]
        try:
            task_id_int: int = int(task_id)
            if task_manager.check_availability(task_id=task_id_int):
                if task_manager.check_status(task_id=task_id_int, status=status):
                    return f"{Fore.YELLOW}Task's status is up to date{Style.RESET_ALL}"
                else:
                    task_manager.update_status(task_id=task_id_int, status=status)
                    return f"{Fore.GREEN}Task updated successfully{Style.RESET_ALL}"
            return f"{Fore.RED}Task doesn't exist{Style.RESET_ALL}"
        except ValueError:
            return f"{Fore.RED}Error: The task ID must be an integer.{Style.RESET_ALL}"
    else:
        return f"{Fore.RED}Invalid action.{Style.RESET_ALL}"


if __name__ == "__main__":
    print(main())
