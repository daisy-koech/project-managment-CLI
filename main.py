import argparse
from utils.storage import load_data, save_data
from models.user import User
from models.project import Project
from models.task import Task

parser = argparse.ArgumentParser(description="Project Managemet Tool")
subparsers = parser.add_subparsers(dest="command")

#users
add_user = subparsers.add_parser("add-user")
add_user.add_argument("--name", required=True)
add_user.add_argument("--email", required=True)

subparsers.add_parser("list-users")

#projects
add_project = subparsers.add_parser("add-project")
add_project.add_argument("--title", required=True)
add_project.add_argument("--description", required=True)
add_project.add_argument("--due-date", required=True)

subparsers.add_parser("list-projects")

#tasks
add_task = subparsers.add_parser("add-task")
add_task.add_argument("--project-title", required=True)
add_task.add_argument("--status", default="Pending")
add_task.add_argument("--assigned_to", required="True")

subparsers.add_parser("list-tasks")

complete_task = subparsers.add_parser("complete-task")
complete_task.add_argument("--title", required=True)

args = parser.parse_args()
data = load_data()

#commands
if args.command == "add-user":
    data["users"].append(User(args.name, args.email).get_data())
    save_data(data)
elif args.command == "list-users":
    for user in data["users"]:
        print(f"{user['name']} - {user['email']}")

elif args.command == "add-project":
    data["projects"].append(Project(args.title, args.description, args.due_date).get_data())
    save_data(data)
elif args.command == "list-projects":
    for project in data["projects"]:
        print(f"{project['title']} | {project['due_date']}")

elif args.command == "add-task":
    data["tasks"].append(Task(args.project_title, args.status, args.assigned_to).get_data())
    save_data(data)
elif args.command == "list-tasks":
    for task in data["tasks"]:
        print(f"{task['project_title']} | {task['status']} | {task['assigned_to']}")
elif args.command == "complete-task":
    for task in data["tasks"]:
        if args.title in (task["project_title"], task["title"]):
            task["status"] = "Completed"
            save_data(data)
            break

#testing
# python main.py add-project --title Website --description "Build portfolio site" --due-date 2026-12-01
# python main.py add-task --project-title Website --status Pending --assigned_to Lispy
# python main.py complete-task --title Website