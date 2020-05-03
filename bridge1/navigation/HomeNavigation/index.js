import React from 'react';
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
