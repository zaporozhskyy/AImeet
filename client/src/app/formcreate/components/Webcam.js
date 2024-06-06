import React, { useCallback, useRef, useState } from "react";
import Webcam from "react-webcam";
import { sendAudioFile } from "@/app/lib/use-session";
import * as FFmpeg from '@ffmpeg/ffmpeg';
// import { createFFmpeg } from "@ffmpeg/ffmpeg";

export default function WebcamVideo() {
  const webcamRef = useRef(null);
  const mediaRecorderRef = useRef(null);
  const [capturing, setCapturing] = useState(false);
  const [recordedChunks, setRecordedChunks] = useState([]);

  const handleDataAvailable = useCallback(
    async({ data }) => {
      if (data.size > 0) {
        setRecordedChunks((prev) => prev.concat(data));
      }
    },
    [setRecordedChunks]
  );

  const handleStartCaptureClick = useCallback(() => {
    setCapturing(true);
    mediaRecorderRef.current = new MediaRecorder(webcamRef.current.stream, {
      mimeType: "video/webm",
    });
    mediaRecorderRef.current.addEventListener(
      "dataavailable",
      handleDataAvailable
    );
    mediaRecorderRef.current.start();
  }, [webcamRef, setCapturing, mediaRecorderRef, handleDataAvailable]);

  const handleStopCaptureClick = useCallback(() => {
    mediaRecorderRef.current.stop();
    setCapturing(false);
  }, [mediaRecorderRef, setCapturing]);

  const handleDownload = useCallback(async() => {
    if (recordedChunks.length) {
      const webmblob = new Blob(recordedChunks, {
        type: "video/webm",
      });
      const webmfile = new File([webmblob], "video.webm", {
        type: webmblob.type
      })
      // // await sendAudioFile(webmfile)
      // const ffmpeg = FFmpeg.createFFmpeg({ log: false });
      // if(!ffmpeg.isLoaded()){
      //   await ffmpeg.load();
      // }

      // const inputName = 'video.webm';
      // const outputName = 'output.mp3';
      // ffmpeg.FS('writeFile', inputName, await fetch(webmblob).then((res) => res.arrayBuffer()));

      // await ffmpeg.run('-i', inputName, outputName);

      // const outputData = ffmpeg.FS('readFile', outputName);



      // const blob = new Blob([outputData.buffer], { type: 'audio/mp3' });

      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      document.body.appendChild(a);
      a.style = "display: none";
      a.href = url;
      a.download = "react-webcam-stream-capture.mp3";
      a.click();
      window.URL.revokeObjectURL(url);
      setRecordedChunks([]);
    }
  }, [recordedChunks]);

  const videoConstraints = {
    width: 420,
    height: 420,
    facingMode: "user",
  };

  return (
    <div className="Container">
      <Webcam
        height={400}
        width={400}
        audio={false}
        mirrored={true}
        ref={webcamRef}
        videoConstraints={videoConstraints}
      />
      {capturing ? (
        <button onClick={handleStopCaptureClick}>Stop Capture</button>
      ) : (
        <button onClick={handleStartCaptureClick}>Start Capture</button>
      )}
      {recordedChunks.length > 0 && (
        <button onClick={handleDownload}>Download</button>
      )}
    </div>
  );
}


