import {
    Navbar as NextUINavbar,
    NavbarContent,
    NavbarMenuToggle,
    NavbarBrand,
    NavbarItem,
  } from "@nextui-org/react";
  
  import { Link } from "@nextui-org/react";
  import { link as linkStyles } from "@nextui-org/theme";
  
  import { siteConfig } from "../../../config/site";
  import NextLink from "next/link";
  import clsx from "clsx";
  
  import { Logo } from "./icons";
  
  export const Navbar = () => {
    return (
      <NextUINavbar maxWidth="xl" position="sticky">
        <NavbarContent className="basis-1/5 sm:basis-full" justify="start">
          <NavbarBrand className="gap-3 max-w-fit">
            <NextLink className="flex justify-start items-center gap-1" href="/">
              <Logo />
              <p className="font-bold text-inherit">AIMeet</p>
            </NextLink>
          </NavbarBrand>
          <div className="hidden lg:flex gap-4 justify-start ml-2 flex-col xl:flex-row xl:items-center ">
            {siteConfig.navItems.map((item) => (
              <NavbarItem key={item.href}>
                <NextLink
                  className={clsx(
                    linkStyles({ color: "foreground" }),
                    "data-[active=true]:text-primary data-[active=true]:font-medium"
                  )}
                  color="foreground"
                  href={item.href}
                >
                  {item.label}
                </NextLink>
              </NavbarItem>
            ))}
            <Link
              href="/sign-up"
              className="flex items-center justify-center rounded-full bg-primary px-3 py-7.5 text-regular text-white duration-300 ease-in-out hover:bg-primaryho"
            >
              Sign-up
            </Link>
          </div>
          
        </NavbarContent>
        <NavbarContent justify="end">
        <div className="hidden lg:flex gap-4 justify-end ml-2 flex-col xl:flex-row xl:items-center ">
            <Link
              href="/formcreate"
              className="flex items-center justify-center rounded-full bg-primary px-3 py-7.5 text-regular text-white duration-300 ease-in-out hover:bg-primaryho"
            >
              Create
            </Link>
          </div>
        </NavbarContent>

  
        {/* <NavbarContent
          className="hidden sm:flex basis-1/5 sm:basis-full"
          justify="end"
        >
          <NavbarItem className="hidden sm:flex gap-2">
            <Link isExternal href='/'>
              <Logo className="text-default-500" />
            </Link>
          </NavbarItem>
        </NavbarContent> */}
  
        <NavbarContent className="sm:hidden basis-1 pl-4" justify="end">
          <Link isExternal href='/'>
            <Logo className="text-default-500" />
          </Link>
          <NavbarMenuToggle />
        </NavbarContent>
      </NextUINavbar>
    );
  };
  