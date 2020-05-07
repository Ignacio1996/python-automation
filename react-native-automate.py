import os

project_name = raw_input('Enter React Native project name: ')

go_dir = 'cd ~ && cd projects && '
init_react_native = 'npx react-native init ' + project_name + ' && '
go_into_app = 'cd ' + project_name + ' && pwd && '
react_navigation = 'npm i react-navigation  @react-navigation/native react-native-reanimated react-native-gesture-handler react-native-screens react-native-safe-area-context @react-native-community/masked-view @react-navigation/stack @react-navigation/drawer && '
ui_kitten = 'npm i @ui-kitten/components@next @eva-design/eva@next react-native-svg @ui-kitten/eva-icons@next && '
pod_install = 'pwd && cd ios && pod install && cd .. && '
firebase = 'npm i firebase && mkdir firebase && touch firebase/index.js && '
auth_navigation = 'mkdir navigation && cd navigation && mkdir AuthNavigation && touch AuthNavigation/index.js && mkdir AppNavigation && touch AppNavigation/index.js && mkdir HomeNavigation && touch HomeNavigation/index.js && cd .. && '
app_components = 'mkdir components && mkdir components/Icons && touch components/Icons/index.js'
screens = 'mkdir screens && cd screens && mkdir Home Login SignUp Profile Details && touch index.js Home/index.js Details/index.js Login/index.js SignUp/index.js Profile/index.js && cd .. && '
start_app = 'pwd && npx react-native run-ios && source ~/.bash_profile && npx react-native run-android && '
init_repo = 'git init && '
open_project = 'code .'

#Command to Build Project
system_command = go_dir + init_react_native + go_into_app + react_navigation + ui_kitten + pod_install + firebase + auth_navigation + screens + start_app + init_repo + open_project
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

# Components
icons_location = app_location + '/components/Icons/index.js'
icons_file = open(icons_location, "w")



app_js = """import 'react-native-gesture-handler';
import React from "react";
import {NavigationContainer} from '@react-navigation/native';
import {createDrawerNavigator} from '@react-navigation/drawer';

import * as eva from '@eva-design/eva';
import { ApplicationProvider, IconRegistry, Layout, Text } from '@ui-kitten/components';
import { EvaIconsPack } from '@ui-kitten/eva-icons';

import {Profile, Login, SignUp} from './screens';

import HomeNavigationStack from './navigation/HomeNavigation';

const Drawer = createDrawerNavigator();

function App() {
  return (
    <>
      <IconRegistry icons={EvaIconsPack} />
      <ApplicationProvider {...eva} theme={eva.light}>
        <NavigationContainer>
          <Drawer.Navigator initialRouteName="Home">
            <Drawer.Screen name="Home" component={HomeNavigationStack} />
            <Drawer.Screen name="Login" component={Login} />
            <Drawer.Screen name="Profile" component={Profile} />
            <Drawer.Screen name="SignUp" component={SignUp} />
          </Drawer.Navigator>
        </NavigationContainer>
      </ApplicationProvider>
    </>
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

import {IconSimpleUsageShowcase} from '../../components/Icons';

import {TouchableOpacity} from 'react-native';

const Stack = createStackNavigator();

const HomeNavigationStack = ({navigation}) => {
  return (
    <Stack.Navigator>
      <Stack.Screen
        options={{
          headerLeft: () => (
            <TouchableOpacity onPress={() => navigation.openDrawer()}>
              <IconSimpleUsageShowcase />
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
import {View, Text} from 'react-native';
import { Button, Icon } from '@ui-kitten/components';

const FacebookIcon = (props) => (
  <Icon name='facebook' {...props} />
);

const LoginButton = () => (
  <Button accessoryLeft={FacebookIcon}>Login with Facebook</Button>
);

function Screen(props) {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Home</Text>
      <LoginButton />
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

icons_screen ="""import React from 'react';
import {StyleSheet} from 'react-native';
import {Icon} from '@ui-kitten/components';

export const IconSimpleUsageShowcase = () => (
  <Icon style={styles.icon} fill="#8F9BB3" name="menu" />
);

const styles = StyleSheet.create({
  icon: {
    width: 32,
    height: 32,
    marginLeft: 10,
  },
});
"""


#Write Files

app_file.write(app_js)
auth_navigation_file.write(authentication_stack)

screens_index_file.write(index_screen)

home_screen_file.write(home_screen)
profile_screen_file.write(default_screen)
signup_screen_file.write(default_screen)
login_screen_file.write(default_screen)
details_screen_file.write(default_screen)

home_navigation_stack_file.write(home_navigation_stack_screen)

icons_file.write(icons_screen)


print('Your project has been initialized with react navigation!')
