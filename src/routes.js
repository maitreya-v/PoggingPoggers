import React from "react";

// Admin Imports
import MainDashboard from "views/admin/default";
import NFTMarketplace from "views/admin/marketplace";
import Profile from "views/admin/profile";
import DataTables from "views/admin/tables";
import RTLDefault from "views/rtl/default";

// Auth Imports
import SignIn from "views/auth/SignIn";

// Icon Imports
import {
  MdHome,
  MdOutlineShoppingCart,
  MdBarChart,
  MdPerson,
  MdLock,
} from "react-icons/md";

const routes = [
  {
    name: "Sales Insights",
    layout: "/admin",
    path: "default",
    icon: <MdBarChart className="w-6 h-6" />,
    // icon: <MdHome className="w-6 h-6" />,
    component: <MainDashboard />,
  },
  {
    name: "Inventory",
    layout: "/admin",
    icon: <MdOutlineShoppingCart className="w-6 h-6" />,
    // icon: <MdBarChart className="w-6 h-6" />,
    path: "data-tables",
    component: <DataTables />,
  },
  {
    name: "Market Dynamics",
    layout: "/admin",
    path: "nft-marketplace",
    icon: <MdBarChart className="w-6 h-6" />,
    component: <NFTMarketplace />,
    secondary: true,
  },
  // {
  //   name: "Profile",
  //   layout: "/admin",
  //   path: "profile",
  //   icon: <MdPerson className="w-6 h-6" />,
  //   component: <Profile />,
  // },
  // {
  //   name: "Sign In",
  //   layout: "/auth",
  //   path: "sign-in",
  //   icon: <MdLock className="w-6 h-6" />,
  //   component: <SignIn />,
  // },
  // {
  //   name: "RTL Admin",
  //   layout: "/rtl",
  //   path: "rtl",
  //   icon: <MdHome className="w-6 h-6" />,
  //   component: <RTLDefault />,
  // },
];
export default routes;
