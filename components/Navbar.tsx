'use client'
import { Search, Bell } from 'lucide-react'

export default function Navbar() {
  return (
    <header className="w-full flex items-center justify-between gap-4 px-4 py-3 bg-transparent sticky top-0 backdrop-blur-md z-20">
      <div className="flex items-center gap-4">
        <div className="text-sm uppercase text-slate-300">Dashboard</div>
      </div>
      <div className="flex items-center gap-3">
        <div className="relative">
          <input aria-label="Search" placeholder="Search ticker or research" className="px-3 py-2 rounded-xl bg-surface text-sm w-64" />
          <div className="absolute right-2 top-1.5 text-slate-400"><Search size={14} /></div>
        </div>
        <button aria-label="Notifications" className="p-2 rounded-md hover:bg-white/2"><Bell size={18} /></button>
        <div className="w-9 h-9 rounded-full bg-slate-700 flex items-center justify-center text-sm">U</div>
      </div>
    </header>
  )
}
