import "@/styles/globals.css";
import "@/styles/print.css";
import type { Metadata } from "next";
import type { ReactNode } from "react";

export const metadata: Metadata = {
  title: "Matematica Viva V5",
  description: "Estrutura unica de licoes com conteudo desacoplado"
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="pt-BR">
      <body>{children}</body>
    </html>
  );
}
