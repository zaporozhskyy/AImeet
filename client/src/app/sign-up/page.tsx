"use client";

import { EyeFilledIcon, EyeSlashFilledIcon } from "../components/icons";
import toast from "react-hot-toast";
import { Button, Input } from "@nextui-org/react";
import { useState } from "react";
import {
  useEffect
} from 'react';
import {
  useRouter
} from 'next/router';
import axios from "axios";
import DefaultLayout from "../layout";
import { title } from "../components/primitives";
import urlPush from "../tools/pushurl";

const Register = () => {

  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const [isPasswordVisible, setIsPasswordVisible] = useState(false);
  const toggleVisibility = () => setIsPasswordVisible(!isPasswordVisible);

  const passwordInput = (
    <Input
      label="Password"
      variant="bordered"
      value={password}
      onValueChange={setPassword}
      isRequired
      endContent={
        <button
          className="focus:outline-none"
          type="button"
          onClick={toggleVisibility}
        >
          {isPasswordVisible ? (
            <EyeSlashFilledIcon className="pointer-events-none text-2xl text-default-400" />
          ) : (
            <EyeFilledIcon className="pointer-events-none text-2xl text-default-400" />
          )}
        </button>
      }
      type={isPasswordVisible ? "text" : "password"}
      className="max-w-xs my-2"
    />
  );
  
  const nameInput = (
    <Input
      label="Name"
      labelPlacement="inside"
      variant="faded"
      value={name}
      onValueChange={setName}
      isRequired
      className="max-w-xs"
      
    />
  );

  const emailInput = (
    <Input
      label="Email"
      variant="bordered"
      value={email}
      onValueChange={setEmail}
      isRequired
      className="max-w-xs"
    />
  );

  const createUser = async () => {
    const response = await axios.post("http://localhost:8000/auth/sign-up", JSON.stringify({
      name: name,
      email: email,
      password: password
    }), {headers: {'Content-Type' : 'application/json' }})
    

    if (response.status === 422) {
      toast.error("Something gone wrong!");
    
      return;
    }
    // }
    urlPush('/');
  };

  const RegisterButton = () => (
    <Button
      radius="full"
      className="bg-slate-400 shadow-lg p-1 m-2"
      isDisabled={!name || !email || !password}
      onClick={createUser}
    >
      Register
    </Button>
  );

  return (
    <div className="mr-3 mt-16 flex flex-col items-center justify-center border-3 border-t-0 border-black">
      {nameInput}
      {emailInput}
      {passwordInput}
      <RegisterButton />
    </div>
  );
};

export default function RegisterPage() {
  return (
    <section className="mr-10 flex flex-col items-center justify-center p-8">
        <h1 className={title()}>Sign up</h1>
        <Register />
      </section>
  );
}
