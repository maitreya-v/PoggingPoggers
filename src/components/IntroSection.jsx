import React from "react";
import BotResponse from "./BotResponse";

const IntroSection = () => {
  return (
    <div id="introsection">
      <h1>
        Ettarra
        {/* <BotResponse response=" - How can I help you ? " /> */}
      </h1>
      <div>
        <h2>
          <BotResponse response=" what would you like to have ? " />
        </h2>
      </div>
    </div>
  );
};

export default IntroSection;
