import * as React from "react";

function SvgHamburgerMenu(props) {
  return (
    <svg
      className="fill-current text-peach"
      height={"100%"}
      width={"100%"}
      overflow="visible"
      xmlns="http://www.w3.org/2000/svg"
      {...props}
    >
      <path d="M4 10h24a2 2 0 000-4H4a2 2 0 000 4zm24 4H4a2 2 0 000 4h24a2 2 0 000-4zm0 8H4a2 2 0 000 4h24a2 2 0 000-4z" />
    </svg>
  );
}

export default SvgHamburgerMenu;
