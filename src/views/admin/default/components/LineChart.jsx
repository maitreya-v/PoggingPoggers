import React from 'react';
import { Line } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  LinearScale,
  CategoryScale,
  PointElement,
  LineElement,
  Filler,
  Tooltip,
  Legend,
} from 'chart.js';

ChartJS.register(
  LinearScale,
  CategoryScale,
  PointElement,
  LineElement,
  Filler,
  Tooltip,
  Legend
);
const data = {
    labels: [
      '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
      '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'
    ],
    datasets: [
      {
        label: 'Pickup',
        data: [32, 63, 119, 47, 19, 12, 8, 25, 37, 49, 58, 76, 66, 50, 89, 71, 93, 94, 84, 59, 38, 31, 67, 51],
        fill: false,
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 2,
        pointBackgroundColor: 'rgba(75, 192, 192, 1)',
        pointRadius: 1,
        pointHoverRadius: 7,
      },{
        label: 'Dining Data',
        data: [367, 325, 416, 102, 30, 22, 4, 47, 44, 74, 59, 92, 78, 148, 110, 101, 163, 288, 270, 288, 257, 250, 320, 409],
        fill: false,
        borderColor: 'rgba(255, 99, 132, 1)',
        borderWidth: 2,
        pointBackgroundColor: 'rgba(255, 99, 132, 1)',
        pointRadius: 1,
        pointHoverRadius: 7,
      },{
        label: 'Delivery',
        data: [19, 26, 11, 15, 12, 11, 10, 4, 9, 6, 12, 30, 9, 22, 19, 38, 46, 40, 15, 10, 12, 27, 26, 44],
        fill: false,
        borderColor: 'rgba(155, 99, 177, 1)',
        borderWidth: 2,
        pointBackgroundColor: 'rgba(155, 99, 177, 1)',
        pointRadius: 1,
        pointHoverRadius: 7,
      },
    ],
  };

const options = {
  scales: {
    x: {
      type: 'category',
    },
    y: {
      beginAtZero: true,
      max: 555,
      ticks: {
        stepSize: 1,
      },
      grid: {
        color: 'rgba(0, 0, 0, 0.1)',
      },
    },
  },
};

export default function LineChart() {
  return <Line data={data} options={options}  />;
}
