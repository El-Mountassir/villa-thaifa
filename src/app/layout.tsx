import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Villa Thaifa - Digital Experience",
  description: "Luxury Guesthouse in Thaifa",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
