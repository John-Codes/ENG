import os
import json
import LLMs as LLM
import shutil
import traceback
# class CreateProject:
debug_mode = True
    
    
def FinTune_create_project():
    # Ask the user for the project name
    if debug_mode:
        project_name = "QABot"
        # If in debug mode, delete the directory first to start fresh
        project_dir_path = os.path.join(os.getcwd(), project_name)
        shutil.rmtree(project_dir_path, ignore_errors=True)

    else:
        project_name = input("What is the name of the project? ")

    # Create a directory with the project name
    project_dir_path = os.path.join(os.getcwd(), project_name)
    os.makedirs(project_dir_path, exist_ok=True)

    # Create a project file inside the directory
    project_file_path = os.path.join(project_dir_path, f"{project_name}.json")
    with open(project_file_path, "w") as project_file:
        # Write a JSON object containing the programming language
        if debug_mode:
            programming_language = "python"
        else:
            programming_language = input("What programming language will the project use? ")
        
        programming_language_json = json.dumps({"programming_language": programming_language})
        project_file.write(programming_language_json)

    print(f"Project file created at {project_file_path}")
    class_maker(project_name, programming_language)


def class_maker(project_name, programming_language):
    classes = {}
    while True:
        if debug_mode:
            class_name = "topics"
            user_class_name = {"ClassName_Topics": method_maker(programming_language)}
            classes[class_name] = user_class_name

        else:
            class_name = input("What is the name of your class?")
            user_class_name = {"ClassName_{class_name}": method_maker(programming_language)}
            classes[class_name] = user_class_name


        continue_creating = input("Do you want to create another class? Y/N ")
        if continue_creating.lower() == 'n':
            break

    # Write to the ProjectName.txt
    project_file_path = os.path.join(os.getcwd(), project_name, f"{project_name}.json")
    with open(project_file_path, "w") as project_file:
        json.dump(classes, project_file)

    print(f"Classes and methods written to {project_file_path}")



def method_maker( programming_language):
    try:
        methods = {}
        while True:

            if debug_mode:
                method_definition = "This method will open a file, read its content and print it."
                method_name = "read_and_print_file"
                ai_improvement = "y"
            else:
                method_name = input("What is your new method name? ")
                method_definition = input("In a step-by-step fashion, describe what the method should do from beginning to end. Include libraries you would like to use. ")
                ai_improvement = input("Would you like to ask AI how to make this code better: Y or N ")

            if ai_improvement.lower() == 'y':
            
            # Convert the dictionary to a JSON-formatted string
                code_update_dto_str = json.dumps(code_update_dto)

                response_str = LLM.Call(f"how can this method instructions be made better following best software engineering practices in {programming_language}: '{method_definition}'. only reply in this Json format:{code_update_dto}. Do not comment", "ChatGPT")
                
                 #Convert the JSON-formatted string to a dictionary
                response = json.loads(response_str)

                print(f"Type of response: {type(response)}")  # Debug line
                print(f"Response content: {response}")  # Debug line

                # Assuming response is in the desired format
                is_code = response["IsCode"]
                if is_code == "True":
                    print(response["Code"])
                    ai_version_choice = input("Do you want to take the AI version of the method description? Y/N ")
                    if ai_version_choice.lower() == 'y':
                        method_definition = response["Code"] # Replacing with AI version

            methods[f"MethodName{method_name}"] = {"description": method_definition}

            is_satisfied = input("If you are satisfied with the method written, you can edit it in the ProjectName.Json and add the AI improvements if you want. Are you satisfied? Y/N ")
            if is_satisfied.lower() == 'y':
                break

        return methods
    
    except Exception as ex :
        print(f"Exception type: {type(ex).__name__}")
        print(f"Exception message: {ex}")
        print("Traceback:")
        traceback.print_exc()

code_update_dto = {
    "IsCode": "True or false if it is code goes here",
    "Code": "Your code Update here",
    "Questions": "Your questions list goes here"
}