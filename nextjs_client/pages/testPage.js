import Header from "../components/Header";
import FailedToGetTabData from "../components/FailedToGetTabData";

export default function TestPage() {
  return (
    <>
      <FailedToGetTabData />
    </>
  );
}

TestPage.getLayout = function getLayout(page) {
  return (
    <>
      <Header isLoginPageOrLoggedIn={false} isFAQPage={false} />
      {page}
    </>
  );
};
