import os

project_name = raw_input('Enter the project name: ')

go_dir = 'cd ~ && cd projects && cd python && '
init_react_native = 'npx react-native init ' + project_name + ' && '
go_into_app = 'cd ' + project_name + ' && pwd && '
react_navigation = 'npm i @react-navigation/native react-native-reanimated react-native-gesture-handler react-native-screens react-native-safe-area-context @react-native-community/masked-view @react-navigation/stack && '
pod_install = 'cd ios && pod install && cd .. && '
firebase = 'npm i firebase && mkdir firebase && touch firebase/index.js && '
auth_navigation = 'mkdir navigation && cd navigation && mkdir AuthNavigation && touch AuthNavigation/index.js && mkdir AppNavigation && touch AppNavigation/index.js && '
start_app = 'npx react-native run-ios && source ~/.bash_profile && npx react-native run-android && '
open_project = 'code .'

#Command to Build Project
system_command = go_dir + init_react_native + go_into_app + react_navigation + pod_install + firebase + auth_navigation + start_app + open_project
print("Full command" + system_command)

#Build project
os.system(system_command)

# Write Files
user = 'nicolas'
location = '/Users/' + user + '/projects/python/' + project_name + '/App.js'
app_file = open(location, "w")

app_js = """
import 'react-native-gesture-handler';
import React, { Component } from "react";
import { Text, View, StyleSheet, Button } from "react-native";
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

function HomeScreen(props) {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Home Screen</Text>
      <Button title="Go to Details" onPress={()=>props.navigation.navigate("Details")}/>
    </View>
  );
}
function DetailsScreen(props) {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Details Screen</Text>
      <Button title="Go to Home" onPress={()=>props.navigation.navigate("Home")}/>
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

authentication_stack = """

"""

app_file.write(app_js)
print('Your project has been initialized with react navigation!')