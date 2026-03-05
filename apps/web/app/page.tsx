import Link from "next/link";

export default function HomePage() {
  return (
    <main className="container">
      <h1>Matematica Viva V5</h1>
      <p>Projeto reiniciado com contrato unico e conteudo desacoplado por licao.</p>
      <ul>
        <li>
          <Link href="/sementes/mv-s-000-o-portal-do-reino">Licao piloto portal</Link>
        </li>
        <li>
          <Link href="/sementes/mv-s-001-a-trindade-na-palma">Licao piloto standard</Link>
        </li>
        <li>
          <Link href="/sementes/mv-s-022-revisao-visual">Licao piloto celebration</Link>
        </li>
      </ul>
    </main>
  );
}
