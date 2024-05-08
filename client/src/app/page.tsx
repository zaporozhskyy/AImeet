"use client"
import Image from "next/image";
import React, {useEffect, useState} from "react";

export default function Home() {
  const [message, setMessage] = useState("Loading")

  useEffect(() => {
    fetch("http://localhost:8080/api/home").then(
      response => response.json()
    ).then(
      (data) => {
        setMessage(data.message)
      }
    ) 
  }, []);
  return ( 
    <h1>{message}</h1>
  );
}
