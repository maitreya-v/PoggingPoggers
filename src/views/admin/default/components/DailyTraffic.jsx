import BarChart from "components/charts/BarChart";
import { barChartDataDailyTraffic } from "variables/charts";
import { barChartOptionsDailyTraffic } from "variables/charts";
import { MdArrowDropUp } from "react-icons/md";
import { MdBarChart } from "react-icons/md";
import Card from "components/card";
const DailyTraffic = () => {
  return (
    <Card extra="pb-7 p-[20px]">
      <div className="flex flex-row justify-between">
        <div className="pt-2 ml-1">
          <p className="text-sm font-medium leading-4 text-gray-600">
            Sales Trend
          </p>
          <p className="text-[34px] font-bold text-navy-700 dark:text-white">
            687{" "}
            <span className="text-sm font-medium leading-6 text-gray-600">
              Customers
            </span>
          </p>
        </div>
        <div className="flex items-start mt-2">
          <div className="flex items-center text-sm text-green-500">
            {/* <MdArrowDropUp className="w-5 h-5" />
            <p className="font-bold"> +2.45% </p> */}
            <button className="!linear z-[1] flex items-center justify-center rounded-lg bg-lightPrimary p-2 text-brand-500 !transition !duration-200 hover:bg-gray-100 active:bg-gray-200 dark:bg-navy-700 dark:text-white dark:hover:bg-white/20 dark:active:bg-white/10">
          <MdBarChart className="w-6 h-6" />
        </button>
          </div>
        </div>
      </div>

      <div className="h-[300px] w-full pt-10 pb-0">
        <BarChart
          chartData={barChartDataDailyTraffic}
          chartOptions={barChartOptionsDailyTraffic}
        />
      </div>
    </Card>
  );
};

export default DailyTraffic;
