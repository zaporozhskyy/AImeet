export type SiteConfig = typeof siteConfig;

export const siteConfig = {
  name: "Next.js + NextUI",
  description: "Make beautiful websites regardless of your design experience.",
  navItems: [
    {
      label: "Home",
      href: "/",
    },
    {
      label: "Login",
      href: "/login",
    }
  ],
  links: {
    github: "https://github.com/nextui-org/nextui",
  },
};
