// import Head from 'next/head'
// import Image from 'next/image'
// import styles from '../styles/Home.module.css'
import {Navigation} from '../components/navigation' 




export default function Home({genericData}) {
  return (
    // <div className="inset-0">
    //   <h1 className="text-purple-500 leading-normal text-center"> Generic data is {genericData} </h1>
    //   <h1 className="text-purple-500 leading-normal">Hello World</h1>
    // </div>
    <Navigation/>

  )
}

export async function getStaticProps(context) {
  return {
    props: {genericData: 5}
  }
}