import React, {useState} from 'react';
import {Form, Input} from 'semantic-ui-react';

export const SearchInfo = () => {
  const [url, u]= useState("");

  return (
    <Form>
      <Form.Field>
      <div class="relative flex w-full flex-wrap items-stretch mb-3">
  <input placeholder="url" value = {url} onChange={e=> u(e.target.value)}type="text" placeholder="Placeholder" class="px-3 py-3 relative rounded text-sm border-0 shadow outline-none focus:outline-none focus:ring w-full pr-10"/>
  <span class="z-10 h-full leading-snug font-normal absolute text-center text-blueGray-300 absolute bg-transparent rounded text-base items-center justify-center w-8 right-0 pr-3 py-3">
    <i class="fas fa-user"></i>
  </span>
</div>
      </Form.Field>
      <Form.Field>  
        <button class="bg-gray-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
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
            window.location.reload()
          }
        }}>submit
        </button>
      </Form.Field>
  </Form>
  );
};