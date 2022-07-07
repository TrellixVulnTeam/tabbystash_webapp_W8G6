import { useState } from "react";

const TableWithTabs = ({ tabs }) => {
  const noTabRows = tabs === undefined || tabs.length === 0;

  function nonEmptyTable() {
    return (
      <table
        className={
          (noTabRows ? "" : "mt-4 ") +
          "w-11/12 h-4/5 block overflow-y-scroll border-collapse"
        }
      >
        <tr className="bg-gray-700">
          <th
            className={
              "w-1/2 pl-6 pt-2 pb-2 border-solid border-4 border-black text-peach"
            }
          >
            Name
          </th>
          <th
            className={
              "w-1/2 pl-6 pt-2 pb-2 border-solid border-4 border-black text-peach"
            }
          >
            Location
          </th>
        </tr>

        <tbody>
          {tabs.map((tab) => {
            return (
              <tr className="bg-gray-700">
                <td className="px-4 sm:h-3 h-2 border-solid border-4 border-black text-white">
                  {tab.tabTitle}
                </td>
                <td className="px-4 sm:h-3 h-2 border-solid border-4 border-black text-white">
                  {tab.tabURL}
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
    );
  }

  function noTabsToShowMessage() {
    return (
      <div>
        <h1 className="text-white text-5xl text-center pb-28">
          No tabs found with that search :(
        </h1>
      </div>
    );
  }

  // Idea to make the table have "fixed" headers, which dont change shape if there are 0 rows -> set the table to be fixed when there are 0 rows?

  return (
    <div
      className={
        (noTabRows ? "justify-center " : "justify-start ") +
        "table-with-tabs-dimensions flex flex-col items-center bg-gray-800"
      }
    >
      {/* {console.log("the data passed into this TableWithTabs is: ", tabs)} */}
      {/* <table>
        <tr className="bg-gray-700 sm:w-[1074px]">
          <th className="sm:w-[537px] pl-6 pt-2 pb-2 border-solid border-4 border-black text-peach">
            Name
          </th>
          <th className="sm:w-[537px] pl-6 pt-2 pb-2 border-solid border-4 border-black text-peach">
            Location
          </th>
        </tr>
      </table> */}
      {/* <tr className="bg-gray-700 w-[1408px]"> */}

      {/* <table className="sm:w-[1079px] sm:h-[722.95px] block overflow-y-scroll border-collapse table-fixed -mb-5">
        <thead>

        <tr className="bg-gray-700 sm:w-[1074px]">
          <th className="sm:w-[537px] pl-6 pt-2 pb-2 border-solid border-4 border-black text-peach">
            Name
          </th>
          <th className="sm:w-[537px] pl-6 pt-2 pb-2 border-solid border-4 border-black text-peach">
            Location
          </th>
        </tr>
        </thead>
        <tbody> */}

      {noTabRows ? noTabsToShowMessage() : nonEmptyTable()}
    </div>
  );
};

export default TableWithTabs;
