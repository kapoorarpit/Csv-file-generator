import React from 'react'
import { Header, ItemHeader} from 'semantic-ui-react';
import { List } from 'semantic-ui-react';

export const Data = ({data})=>{
    return (
        <List>
            {data.map(item=>{
                return(
                    <List.Item key={item.name}>
                        <Header>
                            {item.name}
                        </Header>
                        <li>{item.vote}</li>
                        <li>{item.ratig}</li>
                        <li>{item.num}</li>
                        <li>{item.img}</li>
                    </List.Item>
                );
            })}
        </List>
    );
};