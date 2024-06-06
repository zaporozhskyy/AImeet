"use client"
import { Controller, useForm } from "react-hook-form";
import { Button, Input, User } from "@nextui-org/react";
import { title } from "../components/primitives";
import { UserData } from "../lib/use-session"
import * as sess from "../lib/use-session";
import { doLogin }  from "../lib/use-session"
import urlPush from "../tools/pushurl";

export function Form() {

  if (sess.session.account.is_logged_in) {
    return (
      <>
        <p className="text-lg"> 
          Logged in user: <strong>{sess.session.account.email}</strong>
        </p>
      </>
    );
  }

  return (
    <div className="mt-16">
      <LoginForm />
    </div>
  );
}

function LoginForm() {

  const { control, handleSubmit } = useForm({
    defaultValues: { email: "", password: "" },
  });

  const onSubmit = async (data: any) => {
    const { email, password } = data;
    const user_data: UserData = {
        email: email,
        password: password
    }
    const response = await doLogin({ arg: user_data });
    urlPush('/');
  };

  return (
    <form
      onSubmit={handleSubmit(onSubmit)}
      method="POST"
      className="flex flex-col"
    >
      <Controller
        name="email"
        control={control}
        render={({ field }) => (
          <Input variant="faded" type="email" label="Email" {...field} />
        )}
      />
      <Controller
        name="password"
        control={control}
        render={({ field }) => (
          <Input
            variant="faded"
            type="password"
            label="Password"
            className="my-2"
            {...field}
          />
        )}
      />
      <Button
        type="submit"
        radius="full"
        className="bg-gradient-to-tr from-pink-500 to-yellow-500 text-white shadow-lg justify-center items-center mx-16"
      >
        Login
      </Button>
    </form>
  );
}

export default function LoginFunction() {
  return (
      <section className="flex mr-10 flex-col items-center justify-center p-8">
        <h1 className={title()}>Login</h1>
        <Form />
      </section>
  );
}
