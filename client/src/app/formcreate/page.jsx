"use client"
import WebcamVideo from "./components/Webcam"
import Webcam from "react-webcam";
import FormPage from "./components/form"

const videoConstraints = {
  width: { max: 1500 },
  height: { max: 800 },
  facingMode: "user"
};

export default function form() {
  return (
    <div className="left-7">
    <FormPage/>
    <WebcamVideo/>
    </div>
  )
}