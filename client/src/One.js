import React, { Component, useState, useEffect } from 'react'
import { render } from 'react-dom';

function One(){
    useEffect(()=>{
        fetch("/download").then(response=>
            response.json().then(data=>{
                console.log(data)
            })
        );
      },[]);

      return <div />;
}

export default One
