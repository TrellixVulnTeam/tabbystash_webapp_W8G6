import Image from "next/image";
import SvgHamburgerMenu from "./HamburgerMenu";
import { useEffect, useState } from "react";
import SvgBurgerMenuCancel from "./BurgerMenuCancel";
import Logo from "./Logo";
import Link from "next/link";
import Popup from "reactjs-popup";
import axios from "axios";

const Header = (props) => {
  const [menuDisplay, setMenuDisplay] = useState(false);

  return (
    <>
      <header className="sm:flex sm:justify-between">
        <div className="flex justify-between mx-5 mt-5 items-center">
          <div className="h-8 w-7 mt-2">
            <Logo />
          </div>
          <div className="h-8 w-8">
            {/* toggles hamburger menu's icon in header page when clicked*/}
            <button
              onClick={() => setMenuDisplay(!menuDisplay)}
              className="text-gray-500 hover:text-white block sm:hidden"
            >
              {menuDisplay ? <SvgBurgerMenuCancel /> : <SvgHamburgerMenu />}
            </button>
          </div>
        </div>
        <nav
          className={"mx-3 my-1 py-1 sm:block" + (menuDisplay ? "" : " hidden")}
        >
          <ul className="pt-1 sm:flex">
            <li>
              <Link href="/loginPage">
                <a
                  className={
                    "sm:mt-4 px-2 block text-peach font-semibold text-center rounded hover:bg-gray-300" +
                    (props.isLoginPageOrLoggedIn ? " hidden" : "")
                  }
                >
                  Login
                </a>
              </Link>
            </li>
          </ul>
        </nav>
      </header>
    </>
  );
};

export default Header;
