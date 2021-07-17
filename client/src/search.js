import React, {useState} from 'react';
import {Form, Input, Rating} from 'semantic-ui-react';

export const SearchInfo = () => {
  const [url, u]= useState("");

  return (
    <Form>
      <Form.Field>
          <Input placeholder="url" value = {url} 
          onChange={e=> u(e.target.value)}/>
      </Form.Field>
      <Form.Field>  
        <button 
        onClick={async()=>{
          const value= {url};
          const response = await fetch('/submit_url',{
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(value)
          })
          if (response.ok){
            console.log("response worked!")
          }
        }}>submit
        </button>
      </Form.Field>
  </Form>
  );
};