import Head from "next/head";
import Header from "../components/Header";
//import Hero from "../components/Hero";
import React, { useEffect, useState } from "react";
import axios from "axios";
import MyModal from "../components/MyModal";
import Example from "../components/Example";
import "dotenv/config";
// document.body.classList.add("bg-red-900");
export default function Index() {
  const [tabGroupClicked, setTabGroupClicked] = useState(false);
  // useEffect(() => {
  //   // on component render, change the DOM's body element by adding a tailwindcss utility class to it to change it's color
  //   document.body.classList.add("bg-gray-800");
  // });
  return (
    <>
      {/* <Header /> */}
      {/* <MyModal /> */}

      <div className="flex flex-col justify-between py-3 space-y-2">
        <h1 className="text-white font-semibold text-2xl py-3 mx-3">
          What is TabbyStash?
        </h1>
        <h2 className="text-white py-3 px-3 text-left">
          It lets you save tabs while browsing on the internet so you never lose
          them!
        </h2>
      </div>
      <div className="mt-3 mx-5">
        <h1 className="text-white text-center">How does it work?</h1>
        <h2 className="text-white">1) Make an account at www.tabbystash.com</h2>
        <h2 className="text-white">
          2) Install the Firefox extension and use it to save all your tabs in
          your browser window
        </h2>
        <h2 className="text-white">
          3) Login to your account at www.tabbystash.com to view all your saved
          groups of tabs
        </h2>
        <h2 className="text-white relative tooltip">
          4) Share your groups of tabs with other people! (**Coming soon)
        </h2>
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
        console.log("test in get layout");
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
