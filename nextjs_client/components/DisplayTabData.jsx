import { useState } from "react";
import TabGroup from "./TabGroup";
const DisplayTabData = ({ tabData }) => {
  console.log("the tab data: ", tabData);
  const [userInputForTabGroup, setUserInputForTabGroup] = useState("");
  const [filteredTabData, setFilteredTabData] = useState("");
  var positionToPlaceTabGroupInGrid = 0; // alternates between positions 1 through 4, using the formula: (positionToPlaceTabGroupInGrid % 4) + 1
  function filterTabGroupsByInput() {
    console.log(
      "this is what would be used to filter the tab groups by: ",
      userInputForTabGroup
    );
  }
  return (
    <>
      {/* className="border-2 border-white bg-gray-700 text-gray-900 w-full rounded-md py-3 px-4 focus:outline-none focus:border-peach" */}

      {/* <h1>{tabData[0][0]['tabTitle']}</h1> */}
      <div className="flex flex-col items-center sm:w-full h-screen mt-10">
        <label
          for="userInputForTabGroup"
          className="text-peach text-2xl font-bold"
        >
          Search for tab groups by name:
        </label>
        <input
          className="mt-2 text-white text-xl font-semibold rounded-md px-4 py-4 bg-gray-700 border-2 border-white focus:outline-none focus:border-peach w-full sm:max-w-lg max-w-sm"
          type="text"
          id="userInputForTabGroup"
          name="userInputForTabGroup"
          value={userInputForTabGroup}
          onChange={(event) => {
            setUserInputForTabGroup(event.target.value);
            // filterTabGroupsByInput();
          }}
        />

        <div className="sm:cards-sm sm:justify-evenly cards justify-center w-full sm:max-w-7xl h-5/6 bg-gray-700 border-4 border-white mt-4 px-3 py-3 overflow-y-scroll">
          {/* <div className="flex flex-col justify-center items-center w-full sm:max-w-7xl h-full sm:max-h overflow-hidden bg-yellow-400 mt-4"> */}
          {/* <div className="grid grid-cols-4 grid-flow-row-dense bg-gray-500 px-4 py-4 h-5/6 w-5/6 overflow-y-scroll"> */}
          {/* <div className="flex flex-wrap gap-x-44 bg-gray-700 px-8 py-10 mt-4 w-full sm:max-w-7xl h-4/6 border-4 border-white"> */}
          {/* <div className="grid "> */}

          {/* </div> */}
          {tabData
            .filter((tabGroup) => {
              if (userInputForTabGroup == "") {
                return tabGroup;
              } else if (
                tabGroup.tabGroupName
                  .toLowerCase()
                  .includes(userInputForTabGroup.toLowerCase())
              ) {
                return tabGroup;
              }
            })
            .map((val, key) => {
              return (
                <TabGroup
                  // gridPosition={(positionToPlaceTabGroupInGrid++ % 4) + 1}
                  key={key}
                  tabGroupName={val.tabGroupName}
                  tabGroupData={val.tabGroupData}
                />
              );
            })}
          {/* </div> */}
        </div>

        {/* {tabData.filter((tabGroup) => {

       })} */}
        {/* {tabData.filter()} */}
        {/* <h1>Search through your group of tabs</h1> */}
        {/* <h1 className="text-white font-2xl bg-red-800">test</h1> */}
        {/* <h1 className="text-white font-2xl bg-yellow-500">generic</h1> */}
      </div>
    </>
  );
};

export default DisplayTabData;
