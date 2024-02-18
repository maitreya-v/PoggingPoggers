import CheckTable from "./components/CheckTable";
import Widget from "components/widget/Widget";
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
import {
  columnsDataDevelopment,
  columnsDataCheck,
  columnsDataColumns,
  columnsDataComplex,
} from "./variables/columnsData";
import tableDataDevelopment from "./variables/tableDataDevelopment.json";
import tableDataCheck from "./variables/tableDataCheck.json";
import tableDataColumns from "./variables/tableDataColumns.json";
import tableDataComplex from "./variables/tableDataComplex.json";
import DevelopmentTable from "./components/DevelopmentTable";
import ColumnsTable from "./components/ColumnsTable";
import ComplexTable from "./components/ComplexTable";

const Tables = () => {
  return (
    <div>

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
          icon={<FaFileInvoice className="w-6 h-6" />}
          title={"To be invoiced"}
          subtitle={"$2433"}
        />
      </div>
      <div className="grid h-full grid-cols-1 gap-5 mt-5 md:grid-cols-1">
        <DevelopmentTable
          columnsData={columnsDataDevelopment}
          tableData={tableDataDevelopment}
        />
        <CheckTable columnsData={columnsDataCheck} tableData={tableDataCheck} />
      </div>

      <div className="grid h-full grid-cols-1 gap-5 mt-5 md:grid-cols-1">
        <ColumnsTable
          columnsData={columnsDataColumns}
          tableData={tableDataColumns}
        />

        <ComplexTable
          columnsData={columnsDataComplex}
          tableData={tableDataComplex}
        />
      </div>
    </div>
  );
};

export default Tables;
