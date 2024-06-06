import { User, dataFocusVisibleClasses } from "@nextui-org/react";
import { SessionData, defaultSession } from "./lib";
import axios from "axios";
import { sessionmaker } from "./lib";
import { Blob } from "buffer";

export interface UserData {
  email: string;
  password: string;
};

export interface ReadData {
  name: string;
  email: string;
}

export var session = defaultSession

export async function doLogin({ arg }: { arg: UserData }) {
  try{
    const response = await axios.post("http://localhost:8000/auth/sign-in", JSON.stringify({
        email: arg.email,
        password: arg.password
      }), {headers: {'Content-Type' : 'application/json' }})
    console.log(response.data.account.token)
    sessionmaker.changeId = response.data.id;
    sessionmaker.changeName = response.data.account.name; 
    sessionmaker.changeEmail = response.data.account.email; 
    sessionmaker.changeIsLoggedIn = true; 
    sessionmaker.changeToken = response.data.account.token; 
    sessionmaker.changeCreatedAt = response.data.account.created_at; 
    sessionmaker.changeUpdatedAt = response.data.account.updated_at; 
    }
    catch(error){
      console.log(error)
    }
}

export async function returnUser({ token }: { token: string }) {
  try{
    console.log(token)
    const response = await axios.get("http://localhost:8000/me/",  {headers: {"Authorization": "Bearer " + token}})
    let res: ReadData = {
      name: response.data.name,
      email: response.data.email
    }
    return res
  }
  catch{
    sessionmaker.nullSession();
  }
  
}

export async function sendAudioFile(file: File) {
  const formdata = new FormData();
    formdata.append(
      "file",
      file
    )

  const response = await axios.post("http://localhost:8000/prod/returntext", 
      formdata, {headers: {'Content-Type' : 'video/webm'}})
};
