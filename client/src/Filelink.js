import React, { useState, useEffect } from 'react'
import {CSVLink} from "react-csv";
var randomstring = require("randomstring");

function Link(){

const [data, setdata]= useState([]);

    useEffect(()=>{
        fetch("/download").then(response=>
            response.json().then(data=>{
                setdata(data)
            })
        );

      },[]);
    for(const i in data){
        console.log(data[i])
    } 


    const head= [
        {label: 'name', key: 'name'},
        {label: 'vote', key: 'vote'},
        {label: 'rating', key: 'rating'},
        {label: 'num', key: 'num'},
        {label: 'img', key: 'img'}
    ]

    var q=randomstring.generate({
        length: 6,
        charset: 'alphabetic'
    });
    
    q = q+'.csv'
    console.log(q)

    const csvReport = {
        filename : q,
        headers: head,
        data: data
    }

    return(
        <div><button class="bg-gray-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded py-2 px-4 rounded inline-flex items-center">
        <svg class="fill-current w-4 h-4 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M13 8V2H7v6H2l8 8 8-8h-5zM0 18h20v2H0v-2z"/></svg>
        <span><CSVLink {...csvReport}>Download</CSVLink></span>
      </button>
        </div>
    )
}

export default Link