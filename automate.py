import os

project_name = raw_input('Enter the project name: ')

go_root = 'cd ~ && '
go_projects = 'cd projects && '
go_python = 'cd python && '
create_dir = 'mkdir ' + project_name + ' && '
go_into_dir = 'cd ' + project_name + ' && '
index_file = 'touch index.js && npm init -y && npm i express body-parser && '
open_project = 'code .'

#Command to Build Project
system_command = go_root + go_projects + go_python + create_dir + go_into_dir + index_file + open_project
print(system_command)

#Build project
os.system(system_command)

# Write Files
user = 'nicolas'
location = '/Users/' + user + '/projects/python/' + project_name + '/index.js'
f = open(location, "w")
f.write("console.log('New project!!'); \nconsole.log('The test worked!');")
print('Your project has been initialized!')