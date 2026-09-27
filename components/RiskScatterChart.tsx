'use client'
import React from 'react'
import { ResponsiveContainer, ScatterChart, Scatter, XAxis, YAxis, ZAxis, Tooltip, Legend } from 'recharts'
import { Stock } from '../types'

export default function RiskScatterChart({ data }: { data: Stock[] }) {
  const mapped = data.map((d) => ({ x: d.dividendYield, y: d.payoutRatio, z: d.dividendScore, name: d.ticker, risk: d.risk }))
  return (
    <ResponsiveContainer width="100%" height="100%">
      <ScatterChart>
        <XAxis type="number" dataKey="x" name="Dividend Yield" unit="%" />
        <YAxis type="number" dataKey="y" name="Payout Ratio" unit="%" />
        <ZAxis range={[60, 400]} dataKey="z" />
        <Tooltip cursor={{ strokeDasharray: '3 3' }} />
        <Scatter data={mapped} fill="#00BFA6" />
      </ScatterChart>
    </ResponsiveContainer>
  )
}
