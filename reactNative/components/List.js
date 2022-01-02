import React, { Component } from 'react';
import { AppRegistry, FlatList,  
    StyleSheet, View, Alert } from 'react-native'; 
import { Container, Header, Content, List, ListItem, Thumbnail, Text, Left, Body, Right, Button } from 'native-base';

export default class ListThumbnailExample extends Component {
  render() {
    return (

          <List style={{ flex:1 }}>
            <ListItem thumbnail>
              <Left>
                <Thumbnail square source={require('../assets/images/icon-mountain.png')} />
              </Left>
              <Body>
                <Text>Pico da Nevosa</Text>
                <Text note numberOfLines={1}>Subi o segundo ponto mais alto de Portugal . .</Text>
              </Body>
              <Right>
                <Button transparent>
                  <Text>View</Text>
                </Button>
              </Right>
            </ListItem>
            
            
            <ListItem thumbnail>
              <Left>
                <Thumbnail square source={require('../assets/images/icon-mountain.png')} />
              </Left>
              <Body>
                <Text>Quadro com o pôr-do-sol</Text>
                <Text note numberOfLines={1}>Pintura a óleo com o pôr-do-sol no Gerês . .</Text>
              </Body>
              <Right>
                <Button transparent>
                  <Text>View</Text>
                </Button>
              </Right>
            </ListItem>
            
            <ListItem thumbnail>
              <Left>
                <Thumbnail square source={require('../assets/images/icon-mountain.png')} />
              </Left>
              <Body>
                <Text>Major Minors</Text>
                <Text note numberOfLines={1}>Website com representações de minorias em jornais . .</Text>
              </Body>
              <Right>
                <Button transparent>
                  <Text>View</Text>
                </Button>
              </Right>
            </ListItem>

            <ListItem thumbnail>
              <Left>
                <Thumbnail square source={require('../assets/images/icon-mountain.png')} />
              </Left>
              <Body>
                <Text>Quadro com o pôr-do-sol</Text>
                <Text note numberOfLines={1}>Pintura a óleo com o pôr-do-sol no Gerês . .</Text>
              </Body>
              <Right>
                <Button transparent>
                  <Text>View</Text>
                </Button>
              </Right>
            </ListItem>

            <ListItem thumbnail>
              <Left>
                <Thumbnail square source={require('../assets/images/icon-mountain.png')} />
              </Left>
              <Body>
                <Text>Quadro com o pôr-do-sol</Text>
                <Text note numberOfLines={1}>Pintura a óleo com o pôr-do-sol no Gerês . .</Text>
              </Body>
              <Right>
                <Button transparent>
                  <Text>View</Text>
                </Button>
              </Right>
            </ListItem>
            
            <ListItem thumbnail>
              <Left>
                <Thumbnail square source={require('../assets/images/icon-mountain.png')} />
              </Left>
              <Body>
                <Text>Quadro com o pôr-do-sol</Text>
                <Text note numberOfLines={1}>Pintura a óleo com o pôr-do-sol no Gerês . .</Text>
              </Body>
              <Right>
                <Button transparent>
                  <Text>View</Text>
                </Button>
              </Right>
            </ListItem>            
            <ListItem thumbnail>
              <Left>
                <Thumbnail square source={require('../assets/images/icon-mountain.png')} />
              </Left>
              <Body>
                <Text>Quadro com o pôr-do-sol</Text>
                <Text note numberOfLines={1}>Pintura a óleo com o pôr-do-sol no Gerês . .</Text>
              </Body>
              <Right>
                <Button transparent>
                  <Text>View</Text>
                </Button>
              </Right>
            </ListItem>

            <ListItem thumbnail>
              <Left>
                <Thumbnail square source={require('../assets/images/icon-mountain.png')} />
              </Left>
              <Body>
                <Text>Quadro com o pôr-do-sol</Text>
                <Text note numberOfLines={1}>Pintura a óleo com o pôr-do-sol no Gerês . .</Text>
              </Body>
              <Right>
                <Button transparent>
                  <Text>View</Text>
                </Button>
              </Right>
            </ListItem>

            <ListItem thumbnail>
              <Left>
                <Thumbnail square source={require('../assets/images/icon-mountain.png')} />
              </Left>
              <Body>
                <Text>Quadro com o pôr-do-sol</Text>
                <Text note numberOfLines={1}>Pintura a óleo com o pôr-do-sol no Gerês . .</Text>
              </Body>
              <Right>
                <Button transparent>
                  <Text>View</Text>
                </Button>
              </Right>
            </ListItem>

            <ListItem thumbnail>
              <Left>
                <Thumbnail square source={require('../assets/images/icon-mountain.png')} />
              </Left>
              <Body>
                <Text>Quadro com o pôr-do-sol</Text>
                <Text note numberOfLines={1}>Pintura a óleo com o pôr-do-sol no Gerês . .</Text>
              </Body>
              <Right>
                <Button transparent>
                  <Text>View</Text>
                </Button>
              </Right>
            </ListItem>
            
          </List>

    );
  }
}

const styles = StyleSheet.create({  
    container: {  
        flex: 1,  
    },   
})  
