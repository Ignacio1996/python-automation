import os

project_name = raw_input('Enter the project name: ')

go_root = 'cd ~ && '
go_projects = 'cd projects && '
create_dir = 'mkdir ' + project_name + ' && '
go_into_dir = 'cd ' + project_name + ' && '
index_file = 'touch index.js && npm init -y && npm i express body-parser && '
start_server = 'node index.js && '
deploy_to_heroku = 'heroku login && heroku create && git add . && git commit -m"deploying to heroku" && git push heroku master && '
open_project = 'code .'

#Command to Build Project
system_command = go_root + go_projects + create_dir + go_into_dir + index_file + deploy_to_heroku + open_project
print(system_command)

#Build project
os.system(system_command)

# Write Files
user = 'nicolas'
location = '/Users/' + user + '/projects/' + project_name + '/index.js'
f = open(location, "w")

express = """const express = require("express");
const app = express();

app.get("/", (req, res) => {
  res.send("Hello World!");
});

app.listen(process.env.PORT || 8080, () => {
  console.log("Server started...");
});
"""

f.write(express)
print('Your project has been initialized!')