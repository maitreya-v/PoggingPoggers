import React from "react";

const SvgComponent = ({ w, h, stroke }) => {
  return (
    <svg
      width={w}
      height={h}
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
      strokeWidth={1.5}
      stroke={stroke}
      className="h-6 w-6"
    >
      <path
        d="M6.66662 10.115L12.7946 3.98633L13.7379 4.92899L6.66662 12.0003L2.42395 7.75766L3.36662 6.81499L6.66662 10.115Z"
        fill="white"
      />
    </svg>
  );
};
export default SvgComponent;
