import Header from "../components/Header";
import Link from "next/link";
import axios from "axios";
import { Router, useRouter } from "next/router";
import { useState } from "react";
import GoogleLogin from "react-google-login";

axios.defaults.withCredentials = true;

export default function LoginPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const router = useRouter();
  const loginUser = async (event) => {
    event.preventDefault();

    const paramsForFormData = new URLSearchParams();
    paramsForFormData.append("email", email);
    paramsForFormData.append("password", password);

    await axios
      .post("http://localhost:5000/auth/passLogin", paramsForFormData)
      .then((res) => {
        console.log("the result from logging in: ", res);
        if (res.data.success) {
          console.log("success recieved");
          router.push("/dashboard");
        }
        console.log(res);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  const initiateOAuthGoogle = async () => {
    console.log("initiation started");
    await axios
      .get("http://localhost:5000/authentication/dummy")
      .then((response) => {
        console.log("testing");
        console.log(response);
        window.location = response.data.url;
      })
      .catch((err) => {
        console.log("err");
        console.log(err);
      });
  };

  const responseGoogle = async (response) => {
    console.log("the response in general", response);
    await axios
      .get("http://localhost:5000/auth/testGoogleCallback", {
        headers: {
          Authorization: `${response.code}`,
        },
      })
      .then((responseAuth) => {
        console.log("testing success response", responseAuth);
      })
      .catch((errAuth) => {
        console.log("testing error", errAuth);
      });
  };

  return (
    <>
      <div className="min-h-screen flex flex-col justify-start py-12 px-6">
        <h1 className="text-white text-center text-3xl font-extrabold">
          Sign In
        </h1>
        <h2 className="text-sm text-white font-extrabold text-center py-3">
          Don't have an account?
          <Link href="/signUpPage">
            <a className="text-peach">
              <strong> Sign up</strong>
            </a>
          </Link>
        </h2>
        <div className="py-8 px-6">
          <form
            onSubmit={loginUser}
            className="space-y-6"
            action="http://localhost:5000/auth/passLogin"
            method="POST"
          >
            <div>
              {/*the email address input for the form*/}
              <label
                for="email"
                className="block text-sm font-medium text-white"
              >
                Email address
              </label>
              <div className="mt-2">
                <input
                  id="email"
                  name="email"
                  type="email"
                  value={email}
                  onChange={(event) => {
                    setEmail(event.target.value);
                  }}
                  required
                  className="border-2 border-white bg-gray-700 text-white w-full rounded-md py-3 px-4 focus:outline-none focus:border-peach"
                />
              </div>
            </div>
            <div>
              <label
                for="password"
                className="block text-sm font-medium text-white"
              >
                Password
              </label>
              <div className="mt-2">
                <input
                  id="password"
                  name="password"
                  type="password"
                  value={password}
                  onChange={(event) => {
                    setPassword(event.target.value);
                  }}
                  required
                  className="border-2 border-white bg-gray-700 text-white w-full rounded-md py-3 px-4 focus:outline-none focus:border-peach"
                />
              </div>
            </div>
            <div className="bg-white">
              <button type="submit">Login</button>
            </div>
          </form>
        </div>
        <div className="px-5 py-4">
          <GoogleLogin
            clientId=""
            onSuccess={responseGoogle}
            responseType="code"
          />
        </div>
      </div>
    </>
  );
}

LoginPage.getLayout = function getLayout(page) {
  return (
    <>
      <Header isLoginPageOrLoggedIn={true} isFAQPage={false} />
      {page}
    </>
  );
};
