import os
import json

# class CreateProject:

    
    
def create_project():
    # Ask the user for the project name
    project_name = input("What is the name of the project? ")

    # Create a directory with the project name
    project_dir_path = os.path.join(os.getcwd(), project_name)
    os.makedirs(project_dir_path, exist_ok=True)

    # Create a project file inside the directory
    project_file_path = os.path.join(project_dir_path, f"{project_name}.txt")
    with open(project_file_path, "w") as project_file:
        # Write a JSON object containing the programming language
        programming_language = input("What programming language will the project use? ")
        programming_language_json = json.dumps({"programming_language": programming_language})
        project_file.write(programming_language_json)

    print(f"Project file created at {project_file_path}")

