import { parseISO } from "date-fns";
import {
  format,
  formatInTimeZone,
  utcToZonedTime,
  zonedTimeToUtc,
} from "date-fns-tz";
import { useEffect, useRef, useState } from "react";

const TabGroup = ({ tabGroupName, tabGroupData, gridPosition }) => {
  const timestampTabGroupSaved = tabGroupData.timestampTabGroupSaved;
  const tabs = tabGroupData.tabs;
  const [textCanBeTruncated, setTextCanBeTruncated] = useState(false);

  const tabNameElement = useRef(null);

  // var stylesToApplyToTabGroupName = "text-center w-full absolute top-2/4 left-2/4 -translate-x-2/4 -translate-y-2/4 px-3 text-white font-bold font-mono text-5xl sm:text-3xl"

  const utcTimestamp = zonedTimeToUtc(timestampTabGroupSaved, "UTC");
  const utcTimestampISO8601 = utcTimestamp.toISOString(); //timestamp as an ISO 8601 string; we want an ISO 8601 string so that utcToZonedTime can tell what timezone it needs to convert it's given timestamp to (ie. the ISO 8601 string is UTC, and the user's browser is using America/New York timezone, so utcToZonedTime knows it needs to convert from UTC -> EST). If the ISO 8601 string was a naive timestamp, it would incorrectly convert from UTC to EST in this case.

  const userTimezone = Intl.DateTimeFormat().resolvedOptions().timeZone;

  const amPmTimestamp = formatInTimeZone(
    utcTimestampISO8601,
    userTimezone,
    "hh:mm a zzz"
  );

  function canTabGroupNameBeTruncated(e) {
    console.log("the e is: ", e);
    console.log("the stuff: ", e.offsetWidth, e.scrollWidth);
    return e.offsetWidth < e.scrollWidth;
  }

  // we create a ref with useRef() to keep a reference to the html element that has the tab group name. This is so we can check if it can be truncated or not, each time the window (and as a result the tab groups) gets resized.
  function checkIfTabGroupNameCanBeTruncated() {
    if (canTabGroupNameBeTruncated(tabNameElement.current)) {
      setTextCanBeTruncated(true);
    } else {
      setTextCanBeTruncated(false);
    }
  }

  // when the window is resized, we want to check if the tab group name can be truncated.
  // If it can be, then we want to add a tooltip that shows when you hover over the tab group name.
  // Note: We want a tooltip to show up when hovering over the tab group name, IF AND ONLY IF the text is truncated; otherwise, we don't need it because it's unnecessary.
  useEffect(() => {
    window.addEventListener("resize", checkIfTabGroupNameCanBeTruncated);
    return () => {
      window.removeEventListener("resize", checkIfTabGroupNameCanBeTruncated);
    };
  }, []);

  return (
    <div
      // className={"col-start-" + gridPosition.toString() + " " + "bg-purple-600"}
      className="relative flex flex-col-reverse justify-center items-center bg-gray-800 border-2 border-peach rounded-lg"
    >
      {/* <div className="h-4 w-6"> */}
      {/* <h1
        className={
          (textCanBeTruncated ? "truncate " : "") +
          "text-center w-full absolute top-2/4 left-2/4 -translate-x-2/4 -translate-y-2/4 px-3 text-white font-bold font-mono text-5xl sm:text-3xl"
        }
      >
        {tabGroupName}
      </h1> */}
      <h1
        ref={tabNameElement}
        className={
          (textCanBeTruncated ? "truncate " : "") +
          "text-center w-full px-2 text-white font-bold font-mono text-5xl sm:text-3xl"
        }
      >
        {tabGroupName}
      </h1>
      {/* <h1 className="w-full pb-3 text-center text-white font-bold font-mono text-2xl sm:text-xl">
        {amPmTimestamp.toString()}
      </h1>
      <h1 className="text-white text-center">{innerWidth}</h1> */}
    </div>
  );
};

export default TabGroup;
