import { title, subtitle } from "./components/primitives";
import DefaultLayout from "./layout";

export default function HomePage() {
  return (
      <section className="flex flex-col items-center justify-center gap-4 py-8 md:py-10">
        <div className="inline-block max-w-lg text-center justify-center">
          <h1 className={title()}>Make&nbsp;</h1>
          <h1 className={title({ color: "violet" })}>multifunctional&nbsp;</h1>
          <br />
          <h1 className={title()}>
            forms and rethink your interview experience.
          </h1>
          <h4 className={subtitle({ class: "mt-4" })}>
            Beautiful, fast and modern testings and interviews with AI.
          </h4>
        </div>
      </section>
  );
}
