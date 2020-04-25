import os

project_name = raw_input('Enter the project name: ')

go_root = 'cd ~ && '
go_projects = 'cd projects && '
go_python = 'cd python && '
create_dir = 'mkdir ' + project_name + ' && '
go_into_dir = 'cd ' + project_name + ' && '
index_file = 'touch index.js && '
open_project = 'code .'

system_command = go_root + go_projects + go_python + create_dir + go_into_dir + index_file + open_project
# system_command = 'cd ~ && cd projects && cd python && mkdir ' +  project_name + ' && cd ' + project_name + ' && touch index.js && code .'
print(system_command)
os.system(system_command)
print('Your project has been initialized!')