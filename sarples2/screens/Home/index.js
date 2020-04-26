import React from 'react';
import {View, Text, Button, Platform, StyleSheet} from 'react-native';
function Screen(props) {
  return (
    <View style={{flex: 1, alignItems: 'center', justifyContent: 'center'}}>
      <Text style={styles.text}>Home is like sunshine in the rain</Text>
      <Text style={styles.normalText}>Home is like sunshine in the rain</Text>
      <Text style={styles.textUbuntu}>
        Home is like sunshine in the rainfall
      </Text>
      {/* <Text style={{fontFamily: 'Arial'}}>Home</Text> */}
      <Button
        title="Go to Home"
        onPress={() => props.navigation.navigate('Details')}
      />
    </View>
  );
}
export default Screen;

const styles = StyleSheet.create({
  text: {
    fontFamily: Platform.OS === 'ios' ? 'Roboto-Regular' : 'Roboto-Regular.ttf',
    fontSize: 30,
  },
  textUbuntu: {
    fontFamily: Platform.OS === 'ios' ? 'Ubuntu-Medium' : 'Ubuntu-Medium.ttf',
    fontSize: 30,
  },
  normalText: {
    // fontFamily: 'Georgia',
    fontSize: 30,
  },
});
