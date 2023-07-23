import os
import openai
import LLMs as LLM
from getpass import getpass


def gen_subfolders(description):

    response = LLM.Call(description, "ChatGPT")
    
    #subfolders = response.choices[0].text.strip().split('\n')
    # return subfolders
    return response

def create_directory_structure(project_name, subfolders):
    # Create the main project directory
    os.makedirs(project_name, exist_ok=True)
    # Create the subdirectories
    for folder in subfolders:
        os.makedirs(os.path.join(project_name, folder), exist_ok=True)
    # Create the README file
    with open(os.path.join(project_name, 'README.txt'), 'w') as f:
        f.write(f'Project Name: {project_name}\nProject Description: {", ".join(subfolders)}')


def main():
   gen_subfolders("Make python helloworld program")
 

  

def CreateProject(project_name, project_description):
      # Get user input for project name and description
    project_name = input('Enter the project name: ')

    project_description = input('Enter the project description: ')

    # Get subfolders from OpenAI API
    subfolders = gen_subfolders(project_description)

    # Create directory structure
    create_directory_structure(project_name, subfolders)

if __name__ == "__main__":
    main()
