import os

project_name = raw_input('Enter React Native project name: ')

go_dir = 'cd ~ && cd projects && '
init_react_native = 'npx react-native init ' + project_name + ' && '
go_into_app = 'cd ' + project_name + ' && pwd && '
react_navigation = 'npm i @react-navigation/native react-native-reanimated react-native-gesture-handler react-native-screens react-native-safe-area-context @react-native-community/masked-view @react-navigation/stack @react-navigation/drawer && '
pod_install = 'pwd && cd ios && pod install && cd .. && '
firebase = 'npm i firebase && mkdir firebase && touch firebase/index.js && '
auth_navigation = 'mkdir navigation && cd navigation && mkdir AuthNavigation && touch AuthNavigation/index.js && mkdir AppNavigation && touch AppNavigation/index.js && mkdir HomeNavigation && touch HomeNavigation/index.js && cd .. && '
screens = 'mkdir screens && cd screens && mkdir Home Login SignUp Profile Details && touch index.js Home/index.js Details/index.js Login/index.js SignUp/index.js Profile/index.js && cd .. && '
start_app = 'pwd && npx react-native run-ios && source ~/.bash_profile && npx react-native run-android && '
open_project = 'code .'

#Command to Build Project
system_command = go_dir + init_react_native + go_into_app + react_navigation + pod_install + firebase + auth_navigation + screens + start_app + open_project
print("Full command" + system_command)

#Build project
os.system(system_command)

# Write Files
user = 'nicolas'
app_location = '/Users/' + user + '/projects/' + project_name

# App.js
app_file_location = app_location + '/App.js'
app_file = open(app_file_location, "w")

# Authentication files
auth_navigation_location = app_location + '/navigation/AuthNavigation/index.js'
auth_navigation_file = open(auth_navigation_location, "w")

# Screens
home_screen_location = app_location + '/screens/Home/index.js'
home_screen_file = open(home_screen_location, "w")

login_screen_location = app_location + '/screens/Login/index.js'
login_screen_file = open(login_screen_location, "w")

signup_screen_location = app_location + '/screens/SignUp/index.js'
signup_screen_file = open(signup_screen_location, "w")

profile_screen_location = app_location + '/screens/Profile/index.js'
profile_screen_file = open(profile_screen_location, "w")

details_screen_location = app_location + '/screens/Details/index.js'
details_screen_file = open(details_screen_location, "w")

screens_index_location = app_location + '/screens/index.js'
screens_index_file = open(screens_index_location, "w")

home_navigation_stack_location = app_location + '/navigation/HomeNavigation/index.js'
home_navigation_stack_file = open(home_navigation_stack_location, "w")



app_js = """
import 'react-native-gesture-handler';
import React from "react";
import { NavigationContainer } from '@react-navigation/native';
import { createDrawerNavigator } from '@react-navigation/drawer';

import {Home, Profile, Login, SignUp} from './screens';

import HomeNavigationStack from './navigation/HomeNavigation';

const Drawer = createDrawerNavigator();

function App() {
  return (
    <NavigationContainer>
      <Drawer.Navigator initialRouteName="Home">
        <Drawer.Screen name="Home" component={HomeNavigationStack} />
        <Drawer.Screen name="Login" component={Login} />
        <Drawer.Screen name="Profile" component={Profile} />
        <Drawer.Screen name="SignUp" component={SignUp} />
      </Drawer.Navigator>
    </NavigationContainer>
  );
}

export default App;
"""

authentication_stack = """
import React from 'react';
"""

home_navigation_stack_screen = """import React from 'react';
import {createStackNavigator} from '@react-navigation/stack';
import {Home, Details} from '../../screens';

import {Image, StyleSheet, TouchableOpacity} from 'react-native';

const styles = StyleSheet.create({
  tinyLogo: {
    width: 50,
    height: 50,
  },
});

const Stack = createStackNavigator();

const HomeNavigationStack = ({navigation}) => {
  return (
    <Stack.Navigator>
      <Stack.Screen
        options={{
          headerLeft: () => (
            <TouchableOpacity onPress={() => navigation.openDrawer()}>
              <Image
                style={styles.tinyLogo}
                source={{
                  uri: 'https://static.thenounproject.com/png/696519-200.png',
                }}
              />
            </TouchableOpacity>
          ),
        }}
        name="Home"
        component={Home}
      />
      <Stack.Screen name="Details" component={Details} />
    </Stack.Navigator>
  );
};

export default HomeNavigationStack;
"""

home_screen = """import React from 'react';
import {View, Text, Button} from 'react-native';
function Screen(props) {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Home</Text>
      <Button title="Go to Home" onPress={()=>props.navigation.navigate("Details")}/>
    </View>
  );
}
export default Screen;
"""

default_screen = """import React from 'react';
import {View, Text, Button} from 'react-native';
function Screen(props) {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Default Screen</Text>
      <Button title="Go to Home" onPress={()=>props.navigation.navigate("Home")}/>
    </View>
  );
}
export default Screen;
"""



index_screen = """import React from 'react';
import Home from './Home';
import Profile from './Profile';
import Login from './Login';
import SignUp from './SignUp';
import Details from './Details';

export {Home, Profile, Login, SignUp, Details}
"""

app_file.write(app_js)
auth_navigation_file.write(authentication_stack)

screens_index_file.write(index_screen)

home_screen_file.write(home_screen)
profile_screen_file.write(default_screen)
signup_screen_file.write(default_screen)
login_screen_file.write(default_screen)
details_screen_file.write(default_screen)

home_navigation_stack_file.write(home_navigation_stack_screen)


print('Your project has been initialized with react navigation!')