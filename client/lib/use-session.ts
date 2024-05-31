import useSWR from "swr";
import useSWRMutation from "swr/mutation";
import { SessionData, defaultSession } from "./lib";

const sessionApiRoute = "/api/session";

async function fetchJson<JSON = unknown>(
  input: RequestInfo,
  init?: RequestInit
): Promise<JSON> {
  return fetch(input, {
    headers: {
      accept: "application/json",
      "content-type": "application/json",
    },
    ...init,
  }).then((res) => res.json());
}

type User = {
  email: string;
  password: string;
};

function doLogin(url: string, { arg }: { arg: User }) {
  return fetchJson<SessionData>(url, {
    method: "POST",
    body: JSON.stringify({ email: arg.email, password: arg.password }),
  });
}
export default function useSession() {
  const { data: session, isLoading } = useSWR(
    sessionApiRoute,
    fetchJson<SessionData>,
    {
      fallbackData: defaultSession,
    }
  );

  const { trigger: login } = useSWRMutation(sessionApiRoute, doLogin, {
    revalidate: false,
  });

  return { session, login, isLoading };
}
