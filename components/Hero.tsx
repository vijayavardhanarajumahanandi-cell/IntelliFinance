'use client'
import React from 'react'

export default function Hero() {
  return (
    <section className="card-glass p-8 rounded-2xl grid lg:grid-cols-2 gap-6 items-center">
      <div>
        <div className="text-xs uppercase text-slate-300 tracking-widest">Quantitative Financial Research</div>
        <h1 className="text-4xl lg:text-5xl font-bold tracking-tight mt-4">Intelligent Financial Analytics, Powered by Machine Learning.</h1>
        <p className="mt-4 text-slate-300 max-w-xl">Analyze financial fundamentals, portfolio risk, model drivers, and explainable AI insights through one integrated research platform.</p>
        <div className="mt-6 flex gap-3">
          <a href="/dashboard" className="px-5 py-3 rounded-xl bg-accent text-black font-semibold">Explore IntelliFinance</a>
          <a href="/dashboard" className="px-5 py-3 rounded-xl border border-white/10">View Research</a>
        </div>
      </div>

      <div className="rounded-xl p-4 bg-gradient-to-br from-white/2 to-transparent">
        <div className="bg-surface p-4 rounded-xl card-glass">
          <div className="flex items-center justify-between">
            <div>
              <div className="text-xs text-slate-300">Portfolio Value</div>
              <div className="text-xl font-semibold">$1,234,567</div>
            </div>
            <div className="text-right">
              <div className="text-xs text-slate-300">Market Coverage</div>
              <div className="text-xl font-semibold">35%</div>
            </div>
          </div>

          <div className="mt-4 grid grid-cols-2 gap-3">
            <div className="p-3 rounded-lg bg-[#071826]">
              <div className="text-xs text-slate-300">Avg Dividend Yield</div>
              <div className="font-semibold text-lg">3.2%</div>
            </div>
            <div className="p-3 rounded-lg bg-[#071826]">
              <div className="text-xs text-slate-300">Risk Profile</div>
              <div className="font-semibold text-lg">Moderate</div>
            </div>
          </div>

          <div className="mt-4">
            <div className="text-xs text-slate-300">Feature Importance</div>
            <div className="mt-2 h-12 bg-slate-800 rounded flex items-center overflow-hidden">
              <div style={{width: '42%'}} className="bg-accent h-full" />
              <div style={{width: '28%'}} className="bg-gold h-full" />
              <div style={{width: '20%'}} className="bg-slate-600 h-full" />
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}
