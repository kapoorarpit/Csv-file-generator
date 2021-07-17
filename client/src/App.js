import React, { Component, useState, useEffect } from 'react'
import { render } from 'react-dom';
import One from './One';
import { SearchInfo} from "./search";

function App(){
    return (
        <div>
            <SearchInfo/>
            <One/>
        </div>
    );
}

export default App;
