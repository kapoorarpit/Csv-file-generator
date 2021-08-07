import Link from './Filelink';
import One from './One';
import Navbar from './Head'
import { SearchInfo} from "./search";
import Footer from './Foot'


function App(){
    return (
        <div>
        <nav><Navbar/></nav>
        <div class="min-h-screen px-4 py-10 bg-gray-900  ... ">
        <div class="container mx-auto rounded-full px-20 py-12 bg-white  ...">
        <h1 class="py-8 font-serif ... text-4xl ... font-bold ...">Enter link here</h1>
            <SearchInfo/>
            <br/>
            <Link/>
        </div>
        <div class="container mx-auto py-10"> 
            <One/>
        </div>
        </div>
        <footer><Footer/></footer>
        </div>
    );
}

export default App;


