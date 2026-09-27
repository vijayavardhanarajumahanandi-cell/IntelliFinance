'use client'
import React from 'react'
import { PieChart, Pie, Cell, ResponsiveContainer } from 'recharts'

export default function SectorChart({ data }: { data: { name: string; value: number }[] }) {
  const colors = ['#00BFA6', '#C9A66B', '#5EEAD4', '#7C3AED', '#60A5FA']
  return (
    <ResponsiveContainer width="100%" height="100%">
      <PieChart>
        <Pie data={data} dataKey="value" nameKey="name" innerRadius={40} outerRadius={70} paddingAngle={3}>
          {data.map((_, idx) => (
            <Cell key={idx} fill={colors[idx % colors.length]} />
          ))}
        </Pie>
      </PieChart>
    </ResponsiveContainer>
  )
}
