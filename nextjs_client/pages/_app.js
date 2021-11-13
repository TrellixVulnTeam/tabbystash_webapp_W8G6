import "../styles/globals.css";
import { useRouter } from "next/router";

function MyApp({ Component, pageProps }) {
  const router = useRouter();
  const getLayout = Component.getLayout || ((page) => page);
  return getLayout(<Component {...pageProps} />, router.asPath);
}

export default MyApp;
