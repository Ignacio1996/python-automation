
import React from 'react';
import {createStackNavigator} from '@react-navigation/stack';
import {Home, Details} from '../../screens';

const Stack = createStackNavigator();

const HomeNavigationStack = () => {
  return (
    <Stack.Navigator>
      <Stack.Screen name="Home" component={Home} />
      <Stack.Screen name="Details" component={Details} />
    </Stack.Navigator>
  );
};

export default HomeNavigationStack;
