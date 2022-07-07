import { useState } from "react";
import TabGroup from "./TabGroup";
const DisplayTabData = ({ tabData }) => {
  const [userInputForTabGroup, setUserInputForTabGroup] = useState("");
  const [filteredTabData, setFilteredTabData] = useState("");
  function renderTabGroups() {
    if (tabData.length === 0) {
      // if the tab data is empty, render nothing
      return null;
    }
    return tabData
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
            key={key}
            tabGroupName={val.tabGroupName}
            tabGroupData={val.tabGroupData}
          />
        );
      });
  }
  return (
    <>
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
          }}
        />
        <div className="sm:cards-sm sm:justify-evenly cards justify-center w-full sm:max-w-7xl h-5/6 bg-gray-700 border-4 border-white mt-4 px-3 py-3 overflow-y-scroll">
          {renderTabGroups()}
        </div>
      </div>
    </>
  );
};

export default DisplayTabData;
