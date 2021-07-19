import React, {  useState, useEffect } from 'react'
//import { render } from 'react-dom';
import {Data} from './Data'

function One(){

    const [data, setdata]= useState([]);

    useEffect(()=>{
        fetch("/download1").then(response=>
            response.json().then(data=>{
                setdata(data)
            })
        );
      },[]);
      
      return (
          <div>
              <Data data={data} />
          </div>
    );
}

export default One
