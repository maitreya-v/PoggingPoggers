import React from "react";
import "./NewChat.css";
const NewChat = ({ setChatLog, setShowMenu }) => {
  return (
    <div
      className="sideMenuButton"
      onClick={() => {
        setChatLog([]);
        setShowMenu(false);
      }}
    >
      Ettarra
    </div>
  );
};

export default NewChat;
