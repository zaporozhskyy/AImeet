export interface UserLogged {
  token: string;
  name: string;
  email: string;
  is_logged_in: boolean; 
  created_at: string;
  updated_at: string;
}
export interface SessionData {
  id: string
  account: UserLogged 
}

export const defaultSession: SessionData = {
  id: "",
  account: {
      token: "",
      name: "",
      email: "",
      is_logged_in: false,
      created_at: "",
      updated_at: ""
  }
};

class Session {
  private sessionData: SessionData

  constructor(){
    this.sessionData = defaultSession;
  }

  set changeToken(token: string){
    this.sessionData.account.token = token
  }

  set changeName(name: string){
    this.sessionData.account.name = name
  }

  set changeEmail(email: string){
    this.sessionData.account.email = email
  }

  set changeIsLoggedIn(is_logged_in: boolean){
    this.sessionData.account.is_logged_in = is_logged_in
  }

  set changeCreatedAt(created_at: string){
    this.sessionData.account.created_at = created_at
  }

  set changeUpdatedAt(updated_at: string){
    this.sessionData.account.updated_at = updated_at
  }

  set changeId(id: string){
    this.sessionData.id = id
  }

  get getToken(): string {
    return this.sessionData.account.token
  }

  nullSession(){
    this.sessionData = defaultSession;
  }
}
  
  let sessionmaker: Session;

  declare global {
    var sessionmaker: Session
  }

  if (process.env.NODE_ENV === "production") {
    sessionmaker = new Session();
  } else {
    if (!global.sessionmaker) {
      global.sessionmaker = new Session();
    }
    sessionmaker = global.sessionmaker;
  }

  export { sessionmaker }
