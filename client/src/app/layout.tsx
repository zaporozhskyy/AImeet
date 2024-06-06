import { Navbar } from "./components/navbar";
import type { Metadata } from "next";
import { Inter } from "next/font/google";
import {Providers} from "./providers";
import "./globals.css";


const inter = Inter({ subsets: ["latin"] });

const metadata: Metadata = {
  title: 'AIMeet'
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
    <head>
    <body className="min-h-screen bg-background font-sans antialiased">
    <div className="relative flex flex-col h-screen">
      <div className="border-b-1">
      <Navbar />
      </div>
      <main className="container mx-auto max-w-7xl px-6 flex-grow">
        <Providers>
        {children}
        </Providers>
      </main>
    </div>
    </body>
    </head>
    </html>
  );
}

// export { metadata };