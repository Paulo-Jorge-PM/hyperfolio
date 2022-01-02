import React, { Component } from 'react';
import { Container, Header, Content, Footer, FooterTab, Button, Icon, Text, View, ScrollView } from 'native-base';
import List from './components/List';

export default class FooterTabsIconTextExample extends Component {
  render() {
    return ( 
      <Container>
      
      <Header />




<List>
	<ListItem iconLeft>
		<Icon name='ios-chatboxes' />
		<Text>Simon Mignolet</Text>
	</ListItem>
	<ListItem iconLeft>
		<Icon name='ios-chatboxes' />
		<Text>Simon Mignolet</Text>
	</ListItem>

	<ListItem iconLeft>
		<Icon name='ios-chatboxes' />
		<Text>Simon Mignolet</Text>
	</ListItem>

	<ListItem iconLeft>
		<Icon name='ios-chatboxes' />
		<Text>Simon Mignolet</Text>
	</ListItem>

	<ListItem iconLeft>
		<Icon name='ios-chatboxes' />
		<Text>Simon Mignolet</Text>
	</ListItem>

	<ListItem iconLeft>
		<Icon name='ios-chatboxes' />
		<Text>Simon Mignolet</Text>
	</ListItem>

	<ListItem iconLeft>
		<Icon name='ios-chatboxes' />
		<Text>Simon Mignolet</Text>
	</ListItem>

	<ListItem iconLeft>
		<Icon name='ios-chatboxes' />
		<Text>Simon Mignolet</Text>
	</ListItem>

	<ListItem iconLeft>
		<Icon name='ios-chatboxes' />
		<Text>Simon Mignolet</Text>
	</ListItem>

	<ListItem iconLeft>
		<Icon name='ios-chatboxes' />
		<Text>Simon Mignolet</Text>
	</ListItem>


</List>


<View>      
<ScrollView>
      <List />
</ScrollView>
</View>

        <Content />
        

        
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
      </Container>
    );
  }
}
