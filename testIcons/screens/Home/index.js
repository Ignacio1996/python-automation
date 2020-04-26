import React from 'react';
import {View, Text, Button, Image, StyleSheet} from 'react-native';

function Screen(props) {
  return (
    <View style={{flex: 1, alignItems: 'center', justifyContent: 'center'}}>
      <Text>Home</Text>
      <Button
        title="Go to Home"
        onPress={() => props.navigation.navigate('Details')}
      />
    </View>
  );
}
export default Screen;

