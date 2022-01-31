import Header from "../components/Header";
import Link from "next/link";
import NewAccForm from "../components/NewAccForm";
import { useState } from "react";
import ErrorRegistration from "../components/ErrorRegistration";
import SuccessRegistration from "../components/SuccessRegistration";

export default function SignUpPage() {
  const [successfulRegistration, setSuccessfulRegistration] = useState(-1);
  return (
    <>
      <div className="min-h-screen flex flex-col justify-start py-12 px-6">
        <h1 className="text-white text-center text-3xl font-extrabold">
          Create an account
        </h1>
        <div
          className={
            successfulRegistration == -1 || successfulRegistration == -2
              ? "hidden "
              : "" + "text-white text-center text-2xl"
          }
        >
          {successfulRegistration == 0 ? (
            <ErrorRegistration />
          ) : (
            <SuccessRegistration />
          )}
        </div>
        <NewAccForm setSuccessfulRegistration={setSuccessfulRegistration} />
      </div>
    </>
  );
}

SignUpPage.getLayout = function getLayout(page) {
  return (
    <>
      <Header isLoginPageOrLoggedIn={true} isFAQPage={false} />
      {page}
    </>
  );
};
