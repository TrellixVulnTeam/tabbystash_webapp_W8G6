import Head from "next/head";
import Header from "../components/Header";
//import Hero from "../components/Hero";
import React, { useEffect } from "react";
// document.body.classList.add("bg-red-900");
export default function Index() {
  // useEffect(() => {
  //   // on component render, change the DOM's body element by adding a tailwindcss utility class to it to change it's color
  //   document.body.classList.add("bg-gray-800");
  // });
  return (
    <>
      {/* <Header /> */}
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
        <h2 className="text-white">
          4) Share your groups of tabs with other people! (**Coming soon)
        </h2>
      </div>
    </>
  );
}

Index.getLayout = function getLayout(page, keyFromAppJS) {
  return (
    <>
      <Header
        isLoginPageOrLoggedIn={false}
        isFAQPage={false}
        key={keyFromAppJS}
      />
      {page}
    </>
  );
};
