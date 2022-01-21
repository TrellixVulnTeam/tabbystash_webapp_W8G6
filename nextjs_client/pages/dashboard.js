import axios from "axios";
import Header from "../components/Header";
import { useRouter } from "next/router";

axios.defaults.withCredentials = true;

export default function Dashboard({ data }) {
  return <h1>{data}</h1>;
}

export async function getServerSideProps({ req }) {
  var loggedIn = false;
  const paramsForFormData = new URLSearchParams();
  paramsForFormData.append("email", "garbageData");
  await axios
    .get("http://localhost:5000/auth/isLoggedIn", {
      headers: {
        Cookie: req.headers.cookie,
      },
    })
    .then((res) => {
      console.log("the res is: ", res);
      console.log("was the .then reached?");
      if (res.data.success) {
        console.log("inside res.data.success");
        loggedIn = true;
        // success message returned by the backend API means that the user is logged in and can now
        // if the user IS logged in, make a request for their data to be shown in the /dashboard page
        // if the user IS NOT LOGGED IN, redirect them to the login page
      }
    })
    .catch((err) => {
      console.log(err);
    });
  console.log("this means that the .then wasnt reached");
  if (loggedIn) {
    console.log("was the loggedIn true reached");
    return {
      props: {
        data: "something",
      },
    };
  }
  return {
    // if the user wasn't authenticated by the backend API, then redirect them to the login page
    redirect: {
      permanent: false,
      destination: "/loginPage",
    },
  };

  // return {
  //   // if the user wasn't logged in, they would have been redirected to the login page by this point. So only user information should be passed as a prop at this point
  //   props: { loginStatus: loggedIn }, // Will be passed to the page component as props
  // };
}

Dashboard.getLayout = function getLayout(page, keyFromAppJS) {
  return (
    <>
      <Header
        isLoginPageOrLoggedIn={true}
        isFAQPage={false}
        key={keyFromAppJS}
      />
      {page}
    </>
  );
};
