import { title, subtitle } from "../components/primitives";
import { sessionmaker } from "../lib/lib";
import { returnUser } from "../lib/use-session";

const GetUser = async () => {
    let response: any = ""
    try{
        console.log(sessionmaker.getToken)
        response = await returnUser({token: sessionmaker.getToken})
        
    }
    catch(error){
        console.log(error)
        return (
            <div>
            <h1 className={title({ color: "foreground" })}>You are not logged!&nbsp;</h1>
            </div>
            );
    }
    
    return(
        <div>
            <h1 className={title({ color: "violet" })}>Your profile information:&nbsp;</h1>
            <br />
            <h1 className={title()}>
            Username: ${response.name}
            </h1>
            <h1 className={title()}>
            Email: ${response.email}
            </h1>
            <h4 className={subtitle({ class: "mt-4" })}>
            Beautiful, fast and modern testings and interviews with AI.
            </h4>
            </div>
        )
}

export default function ProfilePage() {
    return(
        <section className="flex flex-col items-center justify-center gap-4 py-8 md:py-10">
        <div className="inline-block max-w-lg text-center justify-center">
        <GetUser />
        </div>
        </section>
    )

}
