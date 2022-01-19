import axios from "axios";
import { useState } from "react";
const NewAccForm = ({ setSuccessfulRegistration }) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const testCORS = async () => {
    await axios
      .get("http://localhost:5000/auth/testCORS", {
        headers: {
          Authorization: "test",
        },
      })
      .then((res) => console.log(res))
      .catch((err) => console.log(err));
  };

  const registerUser = async (event) => {
    event.preventDefault();

    const paramsForFormData = new URLSearchParams();
    paramsForFormData.append("email", email);
    paramsForFormData.append("password", password);

    await axios
      .post("http://localhost:5000/auth/passNewAcc", paramsForFormData)
      .then((res) => {
        console.log(res.data);
        if (res.data.success) {
          setSuccessfulRegistration(1); //render the successful registration div in the signup page
        } else if (res.data.error) {
          setSuccessfulRegistration(0); //if an error JSON message was returned by our server, then we know that the server checked that an email address already belongs to an account
        }
      })
      .catch((err) => {
        console.log(err);
        console.log("i worked");
        setSuccessfulRegistration(-2); //render an error response div in the signup page; this error pops up if there was an issue with the request itself when reaching our server
      });
  };
  return (
    <>
      <div className="py-8 px-6">
        <form
          onSubmit={registerUser}
          className="space-y-6"
          action="http://localhost:5000/auth/passNewAcc"
          method="POST"
        >
          <div>
            {/*the email address input for the form*/}
            <label for="email" class="block text-sm font-medium text-white">
              Email address
            </label>
            <div class="mt-2">
              <input
                id="email"
                name="email"
                type="email"
                value={email}
                onChange={(event) => {
                  setEmail(event.target.value);
                }}
                required
                class="border-2 border-white bg-gray-700 text-gray-900 w-full rounded-md py-3 px-4 focus:outline-none focus:border-peach"
              />
            </div>
          </div>
          <div>
            <label for="password" class="block text-sm font-medium text-white">
              Password
            </label>
            <div class="mt-2">
              <input
                id="password"
                name="password"
                type="password"
                value={password}
                onChange={(event) => {
                  setPassword(event.target.value);
                }}
                required
                class="border-2 border-white bg-gray-700 text-gray-900 w-full rounded-md py-3 px-4 focus:outline-none focus:border-peach"
              />
            </div>
          </div>
          <div className="bg-white w-4 sm:w-5">
            <button type="submit">i am a button</button>
          </div>
        </form>
        <div>
          <button onClick={testCORS}>CORS</button>
        </div>
      </div>
    </>
  );
};

export default NewAccForm;
