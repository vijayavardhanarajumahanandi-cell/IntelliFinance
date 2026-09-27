import { StockTable } from '../../components/StockTable'
import MetricCard from '../../components/MetricCard'
import SectorChart from '../../components/SectorChart'
import { mock } from '../../data/mock'

export default function DashboardPage() {
  return (
    <div className="space-y-6">
      <div>
        <div className="text-sm uppercase text-slate-300">Screening Results</div>
        <h1 className="text-3xl font-bold">Executive Financial Intelligence</h1>
        <p className="text-sm text-slate-300">Research-oriented screening across financial quality, dividend characteristics, and model-derived scoring.</p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <MetricCard label="Top Ranked Stock" value={mock.topStock.ticker} sub={mock.topStock.company} />
        <MetricCard label="Average Dividend Yield" value={`${mock.summary.avgDividendYield}%`} />
        <MetricCard label="Market Coverage" value={`${mock.summary.marketCoverage}%`} />
        <MetricCard label="Sectors Covered" value={`${mock.summary.sectorsCovered}`} />
      </div>

      <div className="grid lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2 card-glass p-4 rounded-2xl">
          <StockTable stocks={mock.stocks} />
        </div>
        <div className="space-y-6">
          <div className="card-glass p-4 rounded-2xl">
            <h3 className="text-sm uppercase text-slate-300">Sector Mix</h3>
            <div className="mt-4 h-48"><SectorChart data={mock.sectorMix} /></div>
          </div>

          <div className="card-glass p-4 rounded-2xl">
            <h3 className="text-sm uppercase text-slate-300">Research Signals</h3>
            <ul className="mt-3 space-y-3">
              {mock.signals.map((s) => (
                <li key={s.title} className="flex items-start gap-3">
                  <div className="w-2 h-8 bg-slate-600 rounded" />
                  <div>
                    <div className="font-semibold">{s.title}</div>
                    <div className="text-sm text-slate-300">{s.desc}</div>
                  </div>
                </li>
              ))}
            </ul>
          </div>
        </div>
      </div>
    </div>
  )
}
