import React from 'react'
import { Header} from 'semantic-ui-react';
import { List } from 'semantic-ui-react';

export const Data = ({data})=>{
    return (
        <List>
            {data.map(item=>{
                return(
                <div class="">
                <div class="rounded-full py-6 px-5... bg-green-300  ...">
                    <List.Item key={item.name}>
                        <li class="px-20 py-3 ui-monospace text-3xl ... font-extrabold ...">
                           Name : {item.name}
                        </li>
                        <li class="px-20 py-1 font-mono ... ui-monospace text-lg ... font-semibold  ...">Votes: {item.vote}</li>
                        <li class="px-20 py-1 font-mono ... ui-monospace text-lg ... font-semibold ...">Ratings: {item.rating}</li>
                        <li class="px-20 py-1 font-mono ... ui-monospace text-lg ... font-semibold ...">Contact-number: {item.num}</li>
                        <li class="px-20 py-1 font-mono ... ui-monospace text-lg ... font-semibold  ...">Image-link: {item.img}</li>
                    </List.Item>
                </div>
                <br/>
                <br/>
                </div>
                );
            })}
        </List>
    );
};