'use client'
import Link from 'next/link'
import { Home, Layers, BarChart, Cpu, Zap } from 'lucide-react'

export default function Sidebar() {
  return (
    <aside className="w-72 hidden lg:flex flex-col gap-6 p-6 card-glass sticky top-6 h-[calc(100vh-48px)]">
      <div className="flex items-center gap-3">
        <div className="w-10 h-10 rounded-xl bg-accent flex items-center justify-center text-black font-bold">IF</div>
        <div>
          <div className="text-lg font-semibold">IntelliFinance</div>
          <div className="text-xs text-slate-300">Quantitative Research</div>
        </div>
      </div>

      <nav className="flex-1">
        <ul className="space-y-2">
          <li><Link href="/" className="flex items-center gap-3 px-3 py-2 rounded-md hover:bg-white/2"> <Home size={16}/> Dashboard</Link></li>
          <li><Link href="/risk" className="flex items-center gap-3 px-3 py-2 rounded-md hover:bg-white/2"> <BarChart size={16}/> Risk & Portfolio</Link></li>
          <li><Link href="/ml-drivers" className="flex items-center gap-3 px-3 py-2 rounded-md hover:bg-white/2"> <Cpu size={16}/> ML Drivers</Link></li>
          <li><Link href="/xai" className="flex items-center gap-3 px-3 py-2 rounded-md hover:bg-white/2"> <Zap size={16}/> Explainable AI</Link></li>
        </ul>
      </nav>

      <div className="text-sm text-slate-400">v0.1 • Demo</div>
    </aside>
  )
}
