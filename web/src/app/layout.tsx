import type { Metadata } from "next";
import { Fira_Code } from "next/font/google";
import "./globals.css";

const firaCode = Fira_Code({
  variable: "--font-fira-code",
  subsets: ["latin"],
  weight: ["400", "500", "600", "700"],
});

export const metadata: Metadata = {
  title: "Claude Code Challenges",
  description: "Interactive challenges to master Claude Code - Anthropic's CLI for Claude",
  keywords: ["Claude Code", "AI", "CLI", "challenges", "learning", "Anthropic"],
  authors: [{ name: "yurekami" }],
  openGraph: {
    title: "Claude Code Challenges",
    description: "Master Claude Code through interactive terminal challenges",
    type: "website",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="dark">
      <body className={`${firaCode.variable} antialiased bg-[#0D1117] text-[#C9D1D9]`}>
        {children}
      </body>
    </html>
  );
}
