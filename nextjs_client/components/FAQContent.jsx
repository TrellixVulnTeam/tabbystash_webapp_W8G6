import Header from "../components/Header";
const FAQContent = () => {
  return (
    <div className="flex flex-col justify-start bg-yellow-500 h-screen">
      <span className="flex flex-col mt-2">
        <h1 className="pl-4 text-white text-left text-2xl bg-blue-600">
          What tech stack was used for this project?
        </h1>
        <span className="text-white ">
          Backend: Flask, PostgreSQL, Redis. Frontend: Next.js, TailwindCSS
        </span>
      </span>
      <h1 className="text-white text-center text-xl bg-blue-600">Test</h1>
      <h1 className="text-white text-center text-xl bg-blue-600">Test</h1>
      <h1 className="text-white text-center text-xl bg-blue-600">Test</h1>
      <h1 className="text-white text-center text-xl bg-blue-600">Test</h1>
    </div>
  );
};

export default FAQContent;
