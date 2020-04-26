
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
