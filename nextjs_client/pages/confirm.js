import Header from "../components/Header";
import { useRouter } from "next/router";
import FailedEmailAuth from "../components/FailedEmailAuth";
import SuccessEmailAuth from "../components/SuccessEmailAuth";
import axios from "axios";
import 'dotenv/config'
var jwt = require("jsonwebtoken");

export default function Confirm({ valid }) {
  const router = useRouter();
  console.log("the value of valid: ", valid);
  return (
    <>
      {/* <div className="text-white ">hi!</div> */}
      {valid == "verified" ? <SuccessEmailAuth /> : <FailedEmailAuth />}
      {/* <FailedEmailAuth /> */}
    </>
  );
}

function verifyEmailValidationJWT(token) {
  return axios({
    method: "post",
    url: {process.env.API_BASE_URL + "/auth/verifyEmailValidationJWT"},
    data: {
      emailToken: token,
    },
  });
}

export async function getServerSideProps({ query }) {
  var response = "";
  const emailVerificationToken = query.verifyToken;
  //jwt.verify(emailVerificationToken);
  await axios({
    method: "post",
    url: process.env.API_BASE_URL + "/auth/verifyEmailValidationJWT",
    data: {
      emailToken: emailVerificationToken,
    },
  })
    .then((res) => {
      console.log(res.data);
      if (res.data.success) {
        response = "verified"; //show a page saying that the account has been successfully verified
      } else {
        response = "unverified"; //show a page saying that the given token is either expired or invalid
      }
    })
    .catch((err) => {
      response = "unverified"; //the .catch case in the promise only happens if theres an issue connecting to our backend server when trying to verify the user account. in this case, the user account has to be unverified since we dont get a response back from our server
      console.log(err);
    });
  // verifyEmailValidationJWT(emailVerificationToken)

  console.log("the token is: ", emailVerificationToken);

  return {
    props: { valid: response }, // will be passed to the page component as props
  };
}

Confirm.getLayout = function getLayout(page) {
  return (
    <>
      <Header isLoginPageOrLoggedIn={false} isFAQPage={false} />
      {page}
    </>
  );
};
