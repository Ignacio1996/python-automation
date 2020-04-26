import React from 'react';
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
