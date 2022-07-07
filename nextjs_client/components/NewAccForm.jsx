import axios from "axios";
import { useState } from "react";

const NewAccForm = ({ setSuccessfulRegistration }) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const registerUser = async (event) => {
    event.preventDefault();

    const paramsForFormData = new URLSearchParams();
    paramsForFormData.append("email", email);
    paramsForFormData.append("password", password);
    await axios
      .post(
        process.env.NEXT_PUBLIC_API_BASE_URL + "/auth/passNewAcc",
        paramsForFormData
      )
      .then((res) => {
        if (res.data.success) {
          setSuccessfulRegistration(1); //render the successful registration div in the signup page
        } else if (res.data.error) {
          setSuccessfulRegistration(0); //if an error JSON message was returned by our server, then we know that the server checked that an email address already belongs to an account
        }
      })
      .catch((err) => {
        setSuccessfulRegistration(-2); //render an error response div in the signup page; this error pops up if there was an issue with the request itself when reaching our server
      });
  };

  return (
    <>
      <div className="px-6">
        <form
          onSubmit={registerUser}
          className="space-y-6"
          action={process.env.NEXT_PUBLIC_API_BASE_URL + "/auth/passNewAcc"}
          method="POST"
        >
          <div className="flex flex-col justify-center items-center">
            {/*the email address input for the form*/}
            <label
              for="email"
              className="w-full sm:max-w-5xl block text-sm font-medium text-white"
            >
              Email address
            </label>
            {/* <div class="mt-2"> */}
            <input
              id="email"
              name="email"
              type="email"
              value={email}
              onChange={(event) => {
                setEmail(event.target.value);
              }}
              required
              className="py-3 px-4 mt-2 w-full sm:max-w-5xl border-2 border-white bg-gray-700 text-white rounded-md focus:outline-none focus:border-peach"
            />
            {/* </div> */}
          </div>
          <div className="flex flex-col justify-center items-center">
            <label
              for="password"
              className="w-full sm:max-w-5xl block text-sm font-medium text-white"
            >
              Password
            </label>
            {/* <div class="mt-2"> */}
            <input
              id="password"
              name="password"
              type="password"
              value={password}
              onChange={(event) => {
                setPassword(event.target.value);
              }}
              required
              className="py-3 px-4 mt-2 w-full sm:max-w-5xl border-2 border-white bg-gray-700 text-white rounded-md focus:outline-none focus:border-peach"
            />
            {/* </div> */}
          </div>
          <div className="w-full flex flex-col justify-center items-center">
            <button
              className="mt-4 w-full sm:max-w-lg px-2 py-3 bg-gray-600 rounded-xl"
              type="submit"
            >
              <span className="text-white font-semibold text-xl">
                Create new account
              </span>
            </button>
          </div>
        </form>
      </div>
    </>
  );
};

export default NewAccForm;
