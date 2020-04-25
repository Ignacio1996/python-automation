import os

project_name = raw_input('Enter the project name: ')

go_dir = 'cd ~ && cd projects && cd python && '
init_react_native = 'npx react-native init ' + project_name
go_into_app = ' && cd ' + project_name + ' && pwd'
start_app = ' && npx react-native run-ios && npx react-native run-android && '
open_project = 'code .'

#Command to Build Project
system_command = go_dir + init_react_native + go_into_app + start_app + open_project
print(system_command)

#Build project
os.system(system_command)

# Write Files
# user = 'nicolas'
# location = '/Users/' + user + '/projects/python/' + project_name + '/index.js'
# f = open(location, "w")

express = """const express = require("express");
const app = express();

app.get("/", (req, res) => {
  res.send("Hello World!");
});

app.listen(process.env.PORT || 8080, () => {
  console.log("Server started...");
});
"""

# f.write(express)
print('Your project has been initialized!')