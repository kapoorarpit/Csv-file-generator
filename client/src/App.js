import React, { Component } from 'react'
import { render } from 'react-dom';
//import One from './One';

class App extends Component{
  constructor(){
      super()
      this.state={}
  }

  postData(){
    alert('are you sure')
  }
  render(){
    return(
    <div>     
        <h2>Search URL</h2>
        <form>
        <label>
        Name:
        <input type="text" name="link" />
        </label>
        <button onClick={ ()=> this.postData()}>Submit</button>
        </form>
    </div>
  )
  }
}

export default App 