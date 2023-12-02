import React, { useEffect } from 'react';
import Highcharts from 'highcharts';
import HighchartsMap from 'highcharts/modules/map';
import axios from 'axios';
import 'highcharts/modules/exporting';

HighchartsMap(Highcharts);

const MapChart = () => {
  useEffect(() => {
    const fetchData = async () => {
      try {
        // Fetch Bangladesh topology data
        const topology = await axios.get(
          'https://code.highcharts.com/mapdata/countries/bd/bd-all.topo.json'
        );

        // Provided demo data
        const demoData = [
          ['bd-da', 66], ['bd-kh', 20], ['bd-ba', 30],
          ['bd-cg', 40], ['bd-sy', 19], ['bd-rj', 11], ['bd-rp', 1]
        ];

        // Create the Highcharts map chart
        Highcharts.mapChart('container', {
          chart: {
            map: topology.data,
          },
          title: {
            text: 'Road Accident Heatmap',
          },
          subtitle: {
            text: 'Source map: <a href="https://code.highcharts.com/mapdata/countries/bd/bd-all.topo.json">Bangladesh</a>',
          },
          mapNavigation: {
            enabled: true,
            buttonOptions: {
              verticalAlign: 'bottom',
            },
          },
          colorAxis: {
            min: 0,
            stops: [
              [0, 'blue'],
              [0.5, 'rgba(255, 255, 0, 0.7)'], // Less solid yellow (opacity: 0.5)
              [1, 'red'],
            ],
          },
          series: [
            {
              data: demoData,
              name: 'Random data',
              states: {
                hover: {
                  color: '#BADA55',
                },
              },
              dataLabels: {
                enabled: true,
                format: '{point.name}',
              },
            },
          ],
        });
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []); 

  return <div id="container" style={{ height: '700px', minWidth: '500px', maxWidth: '800px', margin: '0 auto' }} />;
};

export default MapChart;
