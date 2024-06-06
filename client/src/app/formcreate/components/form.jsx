import React from 'react'
import { useState } from "react";
import { Button, Input } from "@nextui-org/react";

const FormMaker = () => {
    const [field, setField] = useState("");

    const fieldInput = (
        <Input
          label="Your question"
          variant="bordered"
          value={field}
          onValueChange={setField}
          isRequired
          className="max-w-xs"
        />
      );

    const soundField = async () => {
        const utterance = new SpeechSynthesisUtterance(field);
        window.speechSynthesis.speak(utterance);
    }
    const SubmitButton = () => (
      <Button
        radius="full"
        className="bg-gradient-to-tr from-pink-500 to-yellow-500 text-white shadow-lg"
        isDisabled={!field}
        onClick={soundField}
      >
        Submit
      </Button>
    );

    return (
        <div className="mt-6 flex flex-col items-center justify-center">
          {fieldInput}
          <SubmitButton />
        </div>
      );
}
export default function FormPage() {

    

  return (
    <FormMaker />
  )
}
