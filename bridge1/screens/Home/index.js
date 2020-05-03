import React from 'react';
import {View, Text, Button, NativeModules} from 'react-native';

const {Torch} = NativeModules;

function Screen(props) {
  return (
    <View style={{flex: 1, alignItems: 'center', justifyContent: 'center'}}>
      <Text>Home</Text>
      <Button
        title="Go to Home"
        onPress={() => props.navigation.navigate('Details')}
      />
      <Button
        title="Run Native Module"
        onPress={() => {
          Torch.on();
        }}
      />
      <Button
        title="Run Native Module"
        onPress={() => {
          Torch.off();
        }}
      />
    </View>
  );
}
export default Screen;
