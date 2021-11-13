import * as React from "react";

function SvgBurgerMenuCancel(props) {
  return (
    <svg
      className="fill-current text-peach"
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 16 20"
      height={"100%"}
      width={"100%"}
      overflow="visible"
      {...props}
    >
      <path
        d="M9.706 8l5.941-5.941A1.207 1.207 0 0013.941.353L8 6.294 2.059.353A1.207 1.207 0 00.353 2.059L6.294 8 .353 13.941a1.207 1.207 0 001.706 1.706L8 9.706l5.941 5.941a1.205 1.205 0 101.706-1.706L9.706 8"
        fillRule="evenodd"
      />
    </svg>
  );
}

export default SvgBurgerMenuCancel;
