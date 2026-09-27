import RiskScatterChart from '../../components/RiskScatterChart'
import { mock } from '../../data/mock'

export default function RiskPage() {
  return (
    <div className="space-y-6">
      <div>
        <div className="text-sm uppercase text-slate-300">Risk Intelligence</div>
        <h1 className="text-3xl font-bold">Risk Intelligence</h1>
      </div>

      <div className="grid lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2 card-glass p-4 rounded-2xl">
          <h3 className="text-sm uppercase text-slate-300">Dividend Yield vs Payout Ratio</h3>
          <div className="mt-4 h-96"><RiskScatterChart data={mock.stocks} /></div>
        </div>

        <div className="space-y-4">
          <div className="card-glass p-4 rounded-2xl">
            <h4 className="text-sm uppercase text-slate-300">Portfolio Yield</h4>
            <div className="text-2xl font-semibold mt-2">{mock.portfolio.yield}%</div>
            <div className="text-sm text-slate-300 mt-1">Volatility: {mock.portfolio.volatility}%</div>
          </div>

          <div className="card-glass p-4 rounded-2xl">
            <h4 className="text-sm uppercase text-slate-300">Risk Distribution</h4>
            <ul className="mt-3 text-sm text-slate-200">
              <li>Low: {mock.riskDistribution.low}</li>
              <li>Medium: {mock.riskDistribution.medium}</li>
              <li>High: {mock.riskDistribution.high}</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  )
}
