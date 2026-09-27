import React from 'react'

type Props = { label: string; value: string | number; sub?: string }

export default function MetricCard({ label, value, sub }: Props) {
  return (
    <div className="card-glass p-4 rounded-xl">
      <div className="text-xs uppercase text-slate-300">{label}</div>
      <div className="mt-2 flex items-baseline justify-between">
        <div className="text-2xl font-semibold">{value}</div>
      </div>
      {sub && <div className="text-sm text-slate-400 mt-1">{sub}</div>}
    </div>
  )
}
