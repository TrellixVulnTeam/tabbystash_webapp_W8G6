import SvgCatInBox from "./CatInBox";
import Link from "next/link";
const Logo = () => {
  return (
    <>
      <Link href="/">
        <a className="flex items-center w-auto">
          <SvgCatInBox />
          <span className="pb-2 pl-1">
            {/*create padding between the text of the logo button and the cat box icon*/}
            <h1 className="text-peach font-bold text-xl">TabbyStash</h1>
          </span>
        </a>
      </Link>
    </>
  );
};

export default Logo;
