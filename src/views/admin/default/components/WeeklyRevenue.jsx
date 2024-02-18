import Card from "components/card";
import BarChart from "components/charts/BarChart";
import {
  barChartDataWeeklyRevenue,
  barChartOptionsWeeklyRevenue,
} from "variables/charts";
import { MdBarChart } from "react-icons/md";
import LineChart from "./LineChart";

const WeeklyRevenue = () => {
  return (
    <Card extra="flex flex-col bg-white w-full rounded-3xl py-6 px-2 text-center">
      <div className="flex items-center justify-between px-6 mb-auto">
        <h2 className="text-lg font-bold text-navy-700 dark:text-white">
          {/* Weekly Revenue */}
          Hourly Transactions
        </h2>
        <button className="!linear z-[1] flex items-center justify-center rounded-lg bg-lightPrimary p-2 text-brand-500 !transition !duration-200 hover:bg-gray-100 active:bg-gray-200 dark:bg-navy-700 dark:text-white dark:hover:bg-white/20 dark:active:bg-white/10">
          <MdBarChart className="w-6 h-6" />
        </button>
      </div>

      <div className="md:mt-2 lg:mt-0">
        <div className="h-[350px] w-full xl:h-[350px]">
          {/* <BarChart
            chartData={barChartDataWeeklyRevenue}
            chartOptions={barChartOptionsWeeklyRevenue}
          /> */}
          <LineChart />
        </div>
      </div>
    </Card>
  );
};

export default WeeklyRevenue;
