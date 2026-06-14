# Project Management Tool
- This is a Python-based Command-Line Interface (CLI) application for managing users, projects, and tasks.  
- It uses JSON file storage for data persistence.
- The system is built using object-oriented programming and `argparse` for command handling.

## Features
- Add a user
- List all users
- Create a project
- List all projects
- Add a task linked to a project
- List all tasks
- Mark tasks as completed

## Setup instructions
- Clone the repository
- Create virtual environment
```bash
python -m venv venv
```
- Activate the virtual environment
```bash
source venv/bin/activate
```

## How to Run

- Run all commands from the project root folder.
### Adding a user
```bash
python main.py add-user --name "Anne" --email "anne@gmail.com"
```
### List users
```bash
python main.py list-users
```
### Add a project
```bash
python main.py add-project --user-email "anne@gmail.com" --title "CLI Tool" --description "Final project" --due-date "2026-07-01"
```
### List projects
```bash
python main.py list-projects
```
### Add a task
```bash
python main.py add-task --project-title "CLI Tool" --title "Build CLI" --assigned-to "Anne"
```
### List tasks
```bash
python main.py list-tasks
```

### Complete a task
```bash
python main.py complete-task --title "Build CLI"
```