import Header from "../components/Header";
export default function LoginPage() {
  return (
    <>
      <div className="flex items-center justify-center mt-5 h-5 overflow-y-hidden overflow-x-hidden bg-red-500">
        <div>
          <h1>asdasd</h1>
        </div>
      </div>
    </>
  );
}

LoginPage.getLayout = function getLayout(page, keyFromAppJS) {
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
