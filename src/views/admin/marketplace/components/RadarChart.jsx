import React from 'react';
import {
  Chart as ChartJS,
  RadialLinearScale,
  PointElement,
  LineElement,
  Filler,
  Tooltip,
  Legend,
} from 'chart.js';
import { Radar } from 'react-chartjs-2';

ChartJS.register(
  RadialLinearScale,
  PointElement,
  LineElement,
  Filler,
  Tooltip,
  Legend
);

const data = {
  labels: ['Ambience', 'Service', 'Staff', 'Quality', 'Price', 'Portion', 'Cleanliness'],
  datasets: [
    {
      label: 'Tim Hortons',
      data: [2, 9, 3, 5, 2, 3,6],
      backgroundColor: 'rgba(255, 99, 132, 0.2)',
      borderColor: 'rgba(255, 99, 132, 1)',
      borderWidth: 1,
    },{
      label: 'Ettarra',
      data: [4, 3, 6, 5, 2, 4,3],
      backgroundColor: 'rgba(54, 162, 235, 0.2)',
      borderColor: 'rgba(54, 162, 235, 1)',
      borderWidth: 1,
    },{
      label: 'Earth Cafe',
      data: [4, 4, 6, 5, 3, 6, 2],
      backgroundColor: 'rgba(255, 206, 86, 0.2)',
      borderColor: 'rgba(255, 206, 86, 1)',
      borderWidth: 1,
    },{
      label: 'Third Wave',
      data: [7, 2, 6, 5, 7, 5, 4],
      backgroundColor: 'rgba(128, 206, 123, 0.2)',
      borderColor: 'rgba(128, 206, 123, 1)',
      borderWidth: 1,
    }
  ],
};


export function RadarChart() {
  return <Radar data={data} />;
}