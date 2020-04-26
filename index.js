import React, { Component } from "react";
import { Text, View, StyleSheet } from "react-native";

export class App extends Component {
  render() {
    return (
      <View style={styles.container}>
        <Text> Welcome to your new App! </Text>
      </View>
    );
  }
}

export default App;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
});
