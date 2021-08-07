import React from "react";

export default function Navbar({ fixed }) {
  const [navbarOpen, setNavbarOpen] = React.useState(false);
  return (
    <>
      <nav className="relative flex flex-wrap items-center justify-between px-2 bg-blue-500 mb-3 shadow-3xl ...">
      <div className="border-light-blue-500 border-opacity-100 ... shadow-2xl ...">
      <div className="fixed left-0 right-0 bg-white px-10 py-5 shadow-2xl ...">
      <div className="border-2 border-light-blue-500 border-opacity-100 ... shadow-2xl ...">
        <div className="container px-4 mx-auto flex flex-wrap items-center justify-between ">
          <div className="w-full relative flex justify-between lg:w-auto lg:static lg:block lg:justify-start">
            <a
              className="py-8 font-serif ... text-xl ... font-bold ..."
              href="#pablo"
            >
              Get-CSV  
            </a>
            <button
              className="text-white cursor-pointer text-xl leading-none px-3 py-1 border border-solid border-transparent rounded bg-transparent block lg:hidden outline-none focus:outline-none"
              type="button"
              onClick={() => setNavbarOpen(!navbarOpen)}
            >
              <i className="fas fa-bars"></i>
            </button>
          </div>
          <div
            className={
              "lg:flex flex-grow items-center" +
              (navbarOpen ? " flex" : " hidden")
            }
            id="example-navbar-danger"
          >
            <ul className="flex flex-col lg:flex-row list-none lg:ml-auto">
              <li className="nav-item">
                <a
                  className="px-3 py-2 flex items-center text-xs uppercase font-bold leading-snug hover:opacity-75"
                  href="https://github.com/kapoorarpit/go"
                >
                  <i className="fab fa-facebook-square text-lg leading-lg opacity-75"></i><span className="ml-2">Get code</span>
                </a>
              </li>
              <li className="nav-item">
                <a
                  className="px-3 py-2 flex items-center text-xs uppercase font-bold leading-snug hover:opacity-75"
                  href="https://github.com/kapoorarpit"
                >
                  <i className="fab fa-twitter text-lg leading-lg text-gray-100 "></i><span className="ml-2">Github</span>
                </a>
              </li>
              <li className="nav-item">
                <a
                  className="px-3 py-2 flex items-center text-xs uppercase font-bold leading-snug hover:opacity-75"
                  href="https://www.linkedin.com/in/arpit-kapoor---"
                >
                  <i className="fab fa-pinterest text-lg leading-lg opacity-75"></i><span className="ml-2">About</span>
                </a>
              </li>
            </ul>
          </div>
        </div>
        </div>
        </div>
        </div>
      </nav>
      <br/>
      <br/>
    </>
  );
}