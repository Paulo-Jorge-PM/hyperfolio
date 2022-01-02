import React, { Component } from 'react';
import { AppRegistry, FlatList,  
    StyleSheet, View, Alert, Text } from 'react-native'; 
import { Container, Content, Footer, FooterTab, Icon, List, ListItem, Thumbnail, Left, Body, Right, Button } from 'native-base';
import NativeBaseList from './components/List';
import FlatListFormat from './components/Flat-List';


export default class FlatListBasics extends Component {  
  
    render() {  
        return (  
            <View style={styles.container}>  

                <NativeBaseList />
                
        <Footer>
          <FooterTab>
            <Button vertical>
              <Icon name="apps" />
              <Text>Apps</Text>
            </Button>
            <Button vertical>
              <Icon name="camera" />
              <Text>Camera</Text>
            </Button>
            <Button vertical active>
              <Icon active name="navigate" />
              <Text>Navigate</Text>
            </Button>
            <Button vertical>
              <Icon name="person" />
              <Text>Contact</Text>
            </Button>
          </FooterTab>
        </Footer> 
        
            </View>  


        
            
        );  
    }  
}  
  
const styles = StyleSheet.create({  
    container: {  
        flex: 1,  
    },  
    item: {  
        padding: 10,  
        fontSize: 18,  
        height: 44,  
    },  
})  
