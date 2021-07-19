import Link from './Filelink';
import One from './One';
import { SearchInfo} from "./search";


function App(){
    return (
        <div class="min-h-screen px-4 py-10 bg-gray-400  ... ">
        <div class="container mx-auto rounded-full px-20 py-12 bg-green-300  ...">
        <h1 class="py-8 font-serif ... text-4xl ... font-bold ...">Enter link here</h1>
            <SearchInfo/>
            <br/>
            <Link/>
        </div>
        <div class="container mx-auto py-10"> 
            <One/>
        </div>
        </div>
    );
}

export default App;


