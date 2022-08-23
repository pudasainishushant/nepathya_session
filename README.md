## Step 1 : Download and install python and anaconda
## Step 2: Check anaoconda and python version using commands:
python --version
conda --version

## Step 3: Anaconda commands
- List out virtual environments
conda info --envs
- Create a new virtual environment
conda create -n virtual_environment_name python==python__version
- Activate a virtual environment
conda activate virtual_environment_name
- Deactivate virtual environment
conda deactivate

## Python libraries
- Python inbuilt libraries
time math sys
- Third party packages
pandas, numpy
- User built custom package


## Installing python modules
pip install module_name
## Uninstalling python modules
pip uninstall module_name

## Errors
Module not found
ModuleNotFoundError: No module named 'pandas


## Getting all installed libraries
pip list

## Getting all installed libraries in file
pip freeze -> requirements.txt

## ## Getting all installed libraries in file (excluding child dependencies)
- pip install pipreqs
- pipreqs path_of_the_project


# GIT
- Intializing new repository
git init

- Adding files
git add filename-- Adds particular file to staging area
git add .  --- Adds all modifed files in that directory to staging area

- Commiting messages
git commit -m "commit message here"

- Pushing files 
git push origin branch_name

- Branching
- List out all branches
 git branch -a
- Create new branch
 git branch branch_name
- Switch to another branch
 git checkout branch_name

- Pulling changes from repo
git pull origin branch_name
