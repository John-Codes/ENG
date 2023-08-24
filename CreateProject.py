import os
import json

# class CreateProject:

    
    
def FinTune_create_project():
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

def class_maker(project_name):
    classes = {}
    while True:
        class_name = input("What is the name of your class? ")
        user_class_name = {"ClassName{UserClassName}": method_maker()}
        classes[class_name] = user_class_name

        continue_creating = input("Do you want to create another class? Y/N ")
        if continue_creating.lower() == 'n':
            break

    # Write to the ProjectName.txt
    project_file_path = os.path.join(os.getcwd(), project_name, f"{project_name}.json")
    with open(project_file_path, "w") as project_file:
        json.dump(classes, project_file)

    print(f"Classes and methods written to {project_file_path}")

def method_maker():
    methods = {}
    while True:
        method_name = input("What is your new method name? ")
        method_definition = input("In a step-by-step fashion, describe what the method should do from beginning to end. Include libraries you would like to use. ")

        ai_improvement = input("Would you like to ask AI how to make this code better: Y or N ")
        if ai_improvement.lower() == 'y':
            # Here you call the LLM with the prompt
            response = Call(f"how can this method instructions be made better following best software engineering practices in the programming language the user selected?", "ChatGPT")
            # Assuming response is in the desired format
            is_code = response["CodeUpdateDTO"]["IsCode"]
            if is_code == "True":
                print(response["CodeUpdateDTO"]["Code"])
                ai_version_choice = input("Do you want to take the AI version of the method description? Y/N ")
                if ai_version_choice.lower() == 'y':
                    method_definition = response["CodeUpdateDTO"]["Code"] # Replacing with AI version

        methods[f"MethodName{method_name}"] = {"description": method_definition}

        is_satisfied = input("If you are satisfied with the method written, you can edit it in the ProjectName.Json and add the AI improvements if you want. Are you satisfied? Y/N ")
        if is_satisfied.lower() == 'y':
            break

    return methods