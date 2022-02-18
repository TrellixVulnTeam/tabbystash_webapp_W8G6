import axios from "axios";
import { useState } from "react";
var qs = require("qs");

const FailedEmailAuth = () => {
  const [email, setEmail] = useState("");
  const [emailSent, setEmailSent] = useState(false);

  const submitEmail = async (event) => {
    event.preventDefault();
    console.log("test: ", email);
    setEmailSent(true);

    const emailFormData = new URLSearchParams();
    emailFormData.append("email", email);

    await axios
      .post(
        process.env.NEXT_PUBLIC_API_BASE_URL + "/auth/resendVerificationEmail",
        emailFormData
      )
      .then((res) => {
        console.log(res);
        if (res.data.success) {
          console.log("the success: ", res.data.success);
          setTimeout(() => {
            setEmailSent(false);
          }, 5000);
        }
      })
      .catch((err) => {
        console.log(err);
      });
  };

  return (
    <>
      <div className="flex flex-col">
        <div className="text-white text-xl text-center mt-12 font-bold">
          Your account verification link expired or was invalid.
        </div>
        <div className="text-white text-2xl text-center mt-4 font-bold">
          Resend verification link to your email?
        </div>
        <div className="mt-6 mx-auto sm:w-full sm:max-w-md">
          <form
            onSubmit={submitEmail}
            action={
              process.env.NEXT_PUBLIC_API_BASE_URL +
              "/auth/resendVerificationEmail"
            }
            method="POST"
          >
            <label className="block text-white text-sm" htmlFor="email"></label>
            <input
              className="border-2 border-white bg-gray-700 text-white w-full rounded-md py-3 px-4 focus:outline-none focus:border-peach"
              placeholder="example@gmail.com"
              onChange={(event) => {
                setEmail(event.target.value);
              }}
            ></input>
          </form>
        </div>
        <div
          className={
            (!emailSent ? "hidden " : "") +
            "text-green-500 text-2xl text-center mt-4 font-bold"
          }
        >
          Email sent!
        </div>
      </div>
    </>
  );
};
//"border rounded w-full sm:max-sm bg-gray-700"
//"border-2 border-white bg-gray-700 text-gray-900 w-full rounded-md py-3 px-4 focus:outline-none focus:border-peach"
export default FailedEmailAuth;
