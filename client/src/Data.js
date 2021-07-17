import React from 'react'
import { Header} from 'semantic-ui-react';
import { List } from 'semantic-ui-react';

export const Data = ({Data})=>{
    return (
        <List>
            {Data.map(item=>{
                return(
                    <List.Item key={item.name}>
                        <Header>
                            {item.name}
                        </Header>
                    </List.Item>
                );
            })}
        </List>
    );
};