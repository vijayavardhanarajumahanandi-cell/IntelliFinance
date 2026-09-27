'use client'
import React from 'react'
import { Stock } from '../types'

export function StockTable({ stocks }: { stocks: Stock[] }) {
  return (
    <div>
      <div className="flex items-center justify-between mb-4">
        <div className="text-sm text-slate-300">Stock Screening</div>
        <div className="flex items-center gap-2">
          <input placeholder="Search" className="px-2 py-1 rounded bg-surface text-sm" />
          <select className="px-2 py-1 bg-surface rounded text-sm">
            <option>All sectors</option>
          </select>
        </div>
      </div>
      <div className="overflow-x-auto">
        <table className="w-full text-sm table-auto">
          <thead className="text-slate-300">
            <tr>
              <th className="text-left p-2">Rank</th>
              <th className="text-left p-2">Ticker</th>
              <th className="text-left p-2">Company</th>
              <th className="text-left p-2">Sector</th>
              <th className="text-right p-2">Dividend Yield</th>
              <th className="text-right p-2">Dividend Score</th>
              <th className="text-center p-2">Risk Profile</th>
              <th className="text-center p-2">Research Signal</th>
            </tr>
          </thead>
          <tbody>
            {stocks.map((s) => (
              <tr key={s.ticker} className="hover:bg-white/2">
                <td className="p-2">{s.rank}</td>
                <td className="p-2 font-mono">{s.ticker}</td>
                <td className="p-2">{s.company}</td>
                <td className="p-2">{s.sector}</td>
                <td className="p-2 text-right">{s.dividendYield}%</td>
                <td className="p-2 text-right">{s.dividendScore}</td>
                <td className="p-2 text-center"><span className={`px-2 py-1 rounded-full text-xs ${s.risk==='Low'?'bg-green-900':s.risk==='Medium'?'bg-amber-900':'bg-red-900'}`}>{s.risk}</span></td>
                <td className="p-2 text-center">{s.signal}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}
