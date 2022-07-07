import Header from "../components/Header";
import React, { useEffect, useState } from "react";
import axios from "axios";

export default function Index() {
  const [tabGroupClicked, setTabGroupClicked] = useState(false);
  return (
    <>
      <div className="flex flex-col justify-between py-3 space-y-2 mt-5">
        <h1 className="text-white font-semibold text-5xl py-3 mx-3 text-center">
          What is TabbyStash?
        </h1>
        <h2 className="py-3 px-3 text-center text-4xl font-semibold text-peach">
          It lets you save tabs while browsing on the internet so you never lose
          them!
        </h2>
      </div>
      <div className="mt-3 mx-5">
        <h1 className="text-white text-center text-5xl font-bold">
          How does it work?
        </h1>
        <ol className="flex flex-col justify-items items-center mt-6 gap-y-6">
          <li className="text-white text-3xl font-semibold">
            1) Make an account at www.tabbystash.com
          </li>
          <li className="text-white text-3xl font-semibold">
            2) Install the Firefox extension and use it to save all your tabs in
            your browser window
          </li>
          <li className="text-white text-3xl font-semibold">
            3) Login to your account at www.tabbystash.com to view all your
            saved groups of tabs
          </li>
        </ol>
      </div>
      {/* <div class="avatar" data-tooltip="Thinking Cat"></div> */}
    </>
  );
}

// in getserversideprops, check if the user is logged in (isLoggedIn), then pass that prop to the component.
// the component and its given props will be passed to _app.jsx -> at that point, check the props given to the component, and if it has isLoggedIn = true, then pass that to getLayout -> then getLayout can immediately start using it to determine whether to render the "Dashboard" button

export async function getServerSideProps() {
  var isLoggedIn = false;
  await axios
    .get(process.env.API_BASE_URL + "/auth/isLoggedIn")
    .then((res) => {
      if (res.data.success) {
        isLoggedIn = true;
      }
    })
    .catch((err) => {
      console.log(err);
    });
  return {
    props: {
      isLoggedIn: isLoggedIn,
    },
  };
}

Index.getLayout = function getLayout(page, isLoggedIn) {
  return (
    <>
      <Header isLoginPageOrLoggedIn={false} isFAQPage={false} />
      {page}
    </>
  );
};
