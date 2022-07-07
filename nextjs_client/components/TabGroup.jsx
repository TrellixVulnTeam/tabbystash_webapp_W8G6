import {
  format,
  formatInTimeZone,
  utcToZonedTime,
  zonedTimeToUtc,
} from "date-fns-tz";
import { useEffect, useRef, useState } from "react";
import PopupMenu from "./PopupMenu";

const TabGroup = ({ tabGroupName, tabGroupData, gridPosition }) => {
  const timestampTabGroupSaved = tabGroupData.timestampTabGroupSaved;
  const tabs = tabGroupData.tabs;
  const [textCanBeTruncated, setTextCanBeTruncated] = useState(false);
  const [tabMenuOpened, setTabMenuOpened] = useState(false);
  const stylesToApplyToTabGroupNameWithTruncate =
    "truncate text-center w-full px-2 text-white font-bold font-mono text-5xl sm:text-3xl";
  const stylesToApplyToTabGroupNameWithoutTruncate =
    "text-center w-full px-2 text-white font-bold font-mono text-5xl sm:text-3xl";

  const tabNameElement = useRef(null);

  // var stylesToApplyToTabGroupName = "text-center w-full absolute top-2/4 left-2/4 -translate-x-2/4 -translate-y-2/4 px-3 text-white font-bold font-mono text-5xl sm:text-3xl"

  const utcTimestamp = zonedTimeToUtc(timestampTabGroupSaved, "UTC");
  const utcTimestampISO8601 = utcTimestamp.toISOString(); //timestamp as an ISO 8601 string; we want an ISO 8601 string so that utcToZonedTime can tell what timezone it needs to convert it's given timestamp to (ie. the ISO 8601 string is UTC, and the user's browser is using America/New York timezone, so utcToZonedTime knows it needs to convert from UTC -> EST). If the ISO 8601 string was a naive timestamp, it would incorrectly convert from UTC to EST in this case.

  const userTimezone = Intl.DateTimeFormat().resolvedOptions().timeZone;

  const amPmTimestamp = formatInTimeZone(
    utcTimestampISO8601,
    userTimezone,
    "MMM do hh:mm a zzz"
  );

  function canTabGroupNameBeTruncated(e) {
    console.log("the line height is: ", e.clientHeight);
    return e.scrollHeight > e.clientHeight;
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
    checkIfTabGroupNameCanBeTruncated();
    return () => {
      window.removeEventListener("resize", checkIfTabGroupNameCanBeTruncated);
    };
  }, []);

  function belowSmallBreakpoint() {
    // a function to return whether or not the screen is LESS THAN 640PX; TailwindCSS's sm breakpoint targets a min-width size of 640px, so we want to know whether we are below that value or not (ie. if the screen width is 630, 639, etc.)
    return window.screen.width < 640;
  }

  // if the name of the tab group can be truncated (because the text of the tab group name overflows outside of the flex item's dimensions), then we clamp the text at 2 lines, and add an ellipse.
  // We also make the height of the <h1> tag containing the text to be the height of 2 lines worth of text (so if the height of 1 line worth of text is 1rem, we make the height of the h1 tag 2rem to accomodate 2 lines worth of text)
  // if the user is on a screen less than 640px, we want to show 2 lines of text, so we multiply 3rem (the font size given by the text-5xl TailwindCSS utility class) by 2, because the line-height is 1; if the line height of text is 1, then that means the line height is a 1x multiplier of the given font size. Thus, if line-height is 1, and font size is 3rem, the line-height becomes 3rem.
  // So if we want to accomodate 2 lines of text, we need a container of height 6rem ).
  // Note: The text-lg TailwindCSS class gives a line-height of 1.75rem, so to accomodate 2 lines worth of text, we would make the height of the h1 tag 3.50rem if it overflows.
  // TODO (Bug): If the screen is resized from less than 640px to greater than 640px, the height of the h1 tag stays at 6rem, and DOES NOT become 3.50rem. This means that if theres text that overflows, then it will show.
  function stylesToAddIfNameCanBeTruncated() {
    if (textCanBeTruncated) {
      if (belowSmallBreakpoint()) {
        // if the screen width is < 640 px, we need to adjust the height of the html element containing the tab group name -> we do this by adjusting the height to be the size of 2 lines worth of text when the screen width is < 640px
        return "relative tooltip line-clamp-2 h-[6rem] ";
      }
      return "relative tooltip line-clamp-2 h-[3.50rem] ";
    }
    return "h-[1.75rem] ";
  }
  function openTabMenu(e) {
    e.preventDefault();
    setTabMenuOpened(true);
  }
  return (
    <div
      onClick={openTabMenu}
      // onClick={showTabGroupModal}
      className="cursor-pointer flex flex-col justify-center bg-gray-800 border-2 border-peach rounded-lg"
    >
      {tabMenuOpened ? (
        <PopupMenu
          resetTabGroupOnClickState={setTabMenuOpened}
          tabData={tabGroupData}
        />
      ) : null}
      <h1
        ref={tabNameElement}
        className={
          stylesToAddIfNameCanBeTruncated() +
          "px-2 mt-auto break-all text-center text-white font-bold font-mono text-5xl sm:text-lg"
        }
      >
        {tabGroupName}
      </h1>

      <h1 className="mt-auto pb-2 text-center text-white font-bold font-mono text-2xl sm:text-xl">
        {amPmTimestamp.toString()}
      </h1>
    </div>
  );
};

export default TabGroup;
