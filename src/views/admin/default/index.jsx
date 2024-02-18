import MiniCalendar from "components/calendar/MiniCalendar";
import WeeklyRevenue from "views/admin/default/components/WeeklyRevenue";
import TotalSpent from "views/admin/default/components/TotalSpent";
import PieChartCard from "views/admin/default/components/PieChartCard";
import SalesByOrder from "views/admin/default/components/SalesByOrder";
import SalesByPayment from "views/admin/default/components/SalesByPayment";
import { IoMdHome } from "react-icons/io";
import { IoDocuments } from "react-icons/io5";
import { MdBarChart, MdDashboard } from "react-icons/md";
import { FiBarChart2 } from "react-icons/fi";
import { FiBarChart } from "react-icons/fi";
import { FaRupeeSign } from "react-icons/fa";
import { MdAttachMoney } from "react-icons/md";
import { FaShippingFast } from "react-icons/fa";
import { FaFileInvoiceDollar } from "react-icons/fa";
// import { LuPackageOpen } from "react-icons/lu";
import { FaFileInvoice } from "react-icons/fa";
import { FcShipped } from "react-icons/fc";
import { columnsDataCheck, columnsDataComplex } from "./variables/columnsData";

import Widget from "components/widget/Widget";
import CheckTable from "views/admin/default/components/CheckTable";
import ComplexTable from "views/admin/default/components/ComplexTable";
import DailyTraffic from "views/admin/default/components/DailyTraffic";
import LineChart from "./components/LineChart";
import TaskCard from "views/admin/default/components/TaskCard";
import tableDataCheck from "./variables/tableDataCheck.json";
import tableDataComplex from "./variables/tableDataComplex.json";

const Dashboard = () => {
  return (
    <div>
      {/* Card widget */}

      <div className="grid grid-cols-1 gap-5 mt-3 md:grid-cols-2 lg:grid-cols-4 2xl:grid-cols-4 3xl:grid-cols-6">
        <Widget
          icon={<FiBarChart className="h-7 w-7" />}
          title={"Top Selling Item"}
          subtitle={"Baked Vada Pav"}
        />
        <Widget
          icon={<FiBarChart2  className="w-6 h-6" />}
          title={"Low Selling Item"}
          subtitle={"Oat Milk"}
        />
        <Widget
          icon={<FaRupeeSign className="w-6 h-6" />}
          title={"Total Sales"}
          subtitle={"3493386.54"}
        />
        <Widget
          icon={<FaRupeeSign className="h-7 w-7" />}
          title={"Avg Sales/day"}
          subtitle={"$574.34"}
        />
        <Widget
          icon={<FaFileInvoice className="h-7 w-7" />}
          title={"To be packed"}
          subtitle={"145"}
        />
        <Widget
          icon={<FaShippingFast className="w-6 h-6" />}
          title={"To be shipped"}
          subtitle={"$2433"}
        />
        <Widget
          icon={<FcShipped className="w-6 h-6" />}
          title={"To be delivered"}
          subtitle={"$2433"}
        />
        <Widget
          icon={<FaFileInvoice className="w-6 h-6" />}
          title={"To be invoiced"}
          subtitle={"$2433"}
        />
      </div>

      {/* Charts */}

      <div className="grid grid-cols-1 gap-5 mt-5 md:grid-cols-2">
        {/* <TotalSpent /> */}
        <DailyTraffic />
        <WeeklyRevenue />
        {/* <LineChart /> */}
      </div>
      
      {/* Tables & Charts */}

      <div className="grid grid-cols-1 gap-5 mt-5">
        {/* Check Table */}
        {/* <div>
          <CheckTable
            columnsData={columnsDataCheck}
            tableData={tableDataCheck}
          />
        </div> */}

        {/* Traffic chart & Pie Chart */}

        <div className="grid grid-cols-1 gap-5 rounded-[20px] md:grid-cols-3">
          {/* <DailyTraffic /> */}
          {/* <TotalSpent /> */}
          <PieChartCard />
          <SalesByOrder />
          <SalesByPayment />
        </div>

        {/* Complex Table , Task & Calendar */}

        <ComplexTable
          columnsData={columnsDataComplex}
          tableData={tableDataComplex}
        />

        {/* Task chart & Calendar */}
        {/* <div className="grid grid-cols-1 gap-5 rounded-[20px] md:grid-cols-2">
          <TaskCard />
          <div className="grid grid-cols-1 rounded-[20px]">
            <MiniCalendar />
          </div>
        </div> */}
      </div>
    </div>
  );
};

export default Dashboard;
