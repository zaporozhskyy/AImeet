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
      variant="bordered"
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

    // const loginResponse = await login({ email: email, password: password });

    // if (loginResponse.access_token) {
    //   Router.push("/");
    //   toast.success("Signed up!");
    // } else {
    //   toast.error("Failed to register");
    // }
    urlPush('/');
  };

  const RegisterButton = () => (
    <Button
      radius="full"
      className="bg-gradient-to-tr from-pink-500 to-yellow-500 text-white shadow-lg"
      isDisabled={!name || !email || !password}
      onClick={createUser}
    >
      Register
    </Button>
  );

  return (
    <div className="mt-6 flex flex-col items-center justify-center">
      {nameInput}
      {emailInput}
      {passwordInput}
      <RegisterButton />
    </div>
  );
};

export default function RegisterPage() {
  return (
      <div>
        <h1 className={title()}>Sign up</h1>
        <Register />
      </div>
  );
}
