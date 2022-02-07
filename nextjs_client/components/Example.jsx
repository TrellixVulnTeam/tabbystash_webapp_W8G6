/* This example requires Tailwind CSS v2.0+ */
import { Fragment, useRef, useState } from "react";
import { Dialog, Transition } from "@headlessui/react";
import TableWithTabs from "./TableWithTabs";
// import { ExclamationIcon } from "@heroicons/react/outline";

export default function Example({ resetTabGroupOnClickState, tabData }) {
  const [open, setOpen] = useState(true);

  const cancelButtonRef = useRef(null);

  const [userInputForTabs, setUserInputForTabs] = useState("");

  function closeModalAndResetTabGroupOnClickState() {
    setOpen(false);
    resetTabGroupOnClickState(false);
  }

  function filterTabDataByUserInput() {
    return tabData.tabs.filter((tab) => {
      if (userInputForTabs == "") {
        return tab;
      } else if (
        tab.tabTitle.toLowerCase().includes(userInputForTabs.toLowerCase())
      ) {
        return tab;
      }
    });
  }

  return (
    <Transition.Root show={open} as={Fragment}>
      <Dialog
        as="div"
        className="fixed z-10 inset-0 overflow-y-auto"
        initialFocus={cancelButtonRef}
        onClose={closeModalAndResetTabGroupOnClickState}
      >
        <div className="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
          <Transition.Child
            as={Fragment}
            enter="ease-out duration-300"
            enterFrom="opacity-0"
            enterTo="opacity-100"
            leave="ease-in duration-200"
            leaveFrom="opacity-100"
            leaveTo="opacity-0"
          >
            <Dialog.Overlay className="fixed inset-0 bg-gray-500 bg-opacity-30 transition-opacity" />
          </Transition.Child>

          {/* This element is to trick the browser into centering the modal contents. */}
          <span
            className="hidden sm:inline-block sm:align-middle sm:h-screen"
            aria-hidden="true"
          >
            &#8203;
          </span>
          <Transition.Child
            as={Fragment}
            enter="ease-out duration-300"
            enterFrom="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
            enterTo="opacity-100 translate-y-0 sm:scale-100"
            leave="ease-in duration-200"
            leaveFrom="opacity-100 translate-y-0 sm:scale-100"
            leaveTo="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
          >
            {/* sm:max-w-lg sm:w-full */}
            <div className="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle w-[80vw] h-[90vh]">
              <div className="flex flex-col w-full h-full">
                <div className="searchbar-dimensions bg-gray-800">
                  <div className="h-full w-full flex flex-col justify-center items-center">
                    <label
                      for="userInputForTabs"
                      className="text-peach text-xl font-bold px-1 py-1 mt-2"
                    >
                      Search for tabs by name:
                    </label>
                    <input
                      className="text-white text-xl font-semibold rounded-lg px-2 py-1 mt-4 bg-gray-700 border-2 border-white focus:outline-none focus:border-peach w-full sm:max-w-lg max-w-sm"
                      type="text"
                      id="userInputForTabs"
                      name="userInputForTabs"
                      value={userInputForTabs}
                      onChange={(event) => {
                        setUserInputForTabs(event.target.value);
                        // filterTabGroupsByInput();
                        // filterTabDataByUserInput(event.target.value);
                      }}
                    />
                    {/* <h1 className="text-white text-center ">bruh</h1> */}
                  </div>
                </div>
                <TableWithTabs tabs={filterTabDataByUserInput()} />
              </div>
            </div>
          </Transition.Child>
        </div>
      </Dialog>
    </Transition.Root>
  );
}
