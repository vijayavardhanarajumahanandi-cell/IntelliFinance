'use client'
import React from 'react'

export default function ShapContributionChart({ contributions }: { contributions: { feature: string; value: number }[] }) {
  return (
    <div>
      <ul className="space-y-2">
        {contributions.map((c) => (
          <li key={c.feature} className="flex items-center gap-3">
            <div className="w-36 text-sm font-mono">{c.feature}</div>
            <div className="flex-1 h-4 rounded bg-slate-800 overflow-hidden">
              <div style={{ width: `${Math.abs(c.value)*100}%` }} className={`${c.value>0? 'bg-accent' : 'bg-red-600'} h-full`} />
            </div>
            <div className="w-16 text-right text-sm">{c.value>0? `+${c.value.toFixed(2)}`: c.value.toFixed(2)}</div>
          </li>
        ))}
      </ul>
    </div>
  )
}
