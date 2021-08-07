import React from 'react'
import { Header} from 'semantic-ui-react';
import { List } from 'semantic-ui-react';

export const Data = ({data})=>{
    return (
        <div class="">
        <List class="grid grid-cols-3 gap-5">
            {data.map(item=>{
                return(
                <div class="py-4 bg-gray-700 border-double border-4 border-white ...">
                    <List.Item key={item.name}>
                        <li class="px-20 py-3 ui-monospace text-3xl ... font-extrabold ...">
                           Name : {item.name}
                        </li>
                        <div class="px-20 py-1 font-mono ... ui-monospace text-lg ... font-semibold  ...">Votes: {item.vote}</div>
                        <div class="px-20 py-1 font-mono ... ui-monospace text-lg ... font-semibold ...">Ratings: {item.rating}</div>
                        <div class="px-20 py-1 font-mono ... ui-monospace text-lg ... font-semibold ...">Contact-number: {item.num}</div>
                        <img src={item.img} alt="N/A" />
                        {/* <li class="px-20 py-1 font-mono ... ui-monospace text-lg ... font-semibold  ...">Image-link: {item.img}</li> */}
                    </List.Item>
                <br/>
                <br/>
                </div>
                );
            })}
        </List>
        </div>
    );
};