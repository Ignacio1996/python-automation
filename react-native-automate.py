import os

project_name = raw_input('Enter the project name: ')

go_dir = 'cd ~ && cd projects && cd python && '
init_react_native = 'npx react-native init ' + project_name
go_into_app = ' && cd ' + project_name + ' && pwd'
start_app = ' && npx react-native run-ios && source ~/.bash_profile && npx react-native run-android && '
react_navigation = 'npm install @react-navigation/native react-native-gesture-handler react-native-reanimated react-native-screens react-native-safe-area-context @react-navigation/stack && '
open_project = 'code .'

#Command to Build Project
system_command = go_dir + init_react_native + go_into_app + start_app + react_navigation + open_project
print("Full command" + system_command)

#Build project
os.system(system_command)

# Write Files
user = 'nicolas'
location = '/Users/' + user + '/projects/python/' + project_name + '/App.js'
f = open(location, "w")

app_js = """
import React, { Component } from "react";
import { Text, View, StyleSheet } from "react-native";

function HomeScreen() {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Home Screen</Text>
    </View>
  );
}
function DetailsScreen() {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Details Screen</Text>
    </View>
  );
}

const Stack = createStackNavigator();

function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home">
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="Details" component={DetailsScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

export default App;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
});
"""

f.write(app_js)
print('Your project has been initialized with react navigation!')