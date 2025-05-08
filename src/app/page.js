'use client'

import React, {useEffect, useState} from 'react';
import {DeckGL, BitmapLayer } from 'deck.gl';
import {Map} from 'react-map-gl/mapbox';
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css"
const TOKEN = process.env.NEXT_PUBLIC_MAPBOX_TOKEN;
console.log(TOKEN)
const VIEW_STATE = {
  longitude: -115.84499633244127,
  latitude: 33.27923736379083,
  zoom: 8
}
export default function Home() {
  const [selectedDate, setSelectedDate] = useState(new Date('2024-11-03'));
  const disableDateRanges = [
    {start: new Date('2024-11-26'), end: new Date('2024-12-31')}
  ]
  const handleDateChange = (date) => {
    setSelectedDate(date);
  };

  const [imageUrl, setImageUrl] = useState(null);
  useEffect(()=>{
    const formatted_date = selectedDate.toLocaleDateString('en-CA').split("T")[0].replace(/-/g,"_")
    setImageUrl(`http://localhost:8000/image?t=${formatted_date}`);
  }, [selectedDate])
  const layers = [
    imageUrl &&
    new BitmapLayer({
      id: "bitmap-layer",
      bounds: [-116.67880473511462,
        32.572620073389686,
        -115.01118792976791,
        33.985854654191975],
      image: imageUrl,

    })
  ];
  return (
    <>
    <div style = {{position:'fixed', zIndex: 1000, margin:'40px'}}>
    <DatePicker
    selected={selectedDate}
    onChange={handleDateChange}
    dateFormat='M/dd/yyyy'
    excludeDateIntervals={disableDateRanges}
    />
    </div>
    <DeckGL
      initialViewState={VIEW_STATE}
      controller={true}
      layers={layers}
    >
      <Map
        mapboxAccessToken={TOKEN}
        mapStyle="mapbox://styles/mapbox/streets-v11"
      />
    </DeckGL>
   </>
  );
}
