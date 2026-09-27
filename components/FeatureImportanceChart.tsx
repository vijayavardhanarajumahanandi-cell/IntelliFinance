'use client'
import React from 'react'
import { BarChart, Bar, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer } from 'recharts'

export default function FeatureImportanceChart({ rf, xgb }: { rf: { name: string; value: number }[]; xgb: { name: string; value: number }[] }) {
  // merge by name
  const names = Array.from(new Set([...rf.map(r=>r.name), ...xgb.map(x=>x.name)]))
  const data = names.map((n)=>({
    name: n,
    rf: rf.find(r=>r.name===n)?.value ?? 0,
    xgb: xgb.find(x=>x.name===n)?.value ?? 0
  }))
  return (
    <ResponsiveContainer width="100%" height={300}>
      <BarChart data={data} layout="vertical">
        <XAxis type="number" />
        <YAxis dataKey="name" type="category" />
        <Tooltip />
        <Legend />
        <Bar dataKey="rf" fill="#00BFA6" />
        <Bar dataKey="xgb" fill="#C9A66B" />
      </BarChart>
    </ResponsiveContainer>
  )
}
