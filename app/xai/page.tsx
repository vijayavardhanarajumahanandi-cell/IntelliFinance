import ShapContributionChart from '../../components/ShapContributionChart'
import { mock } from '../../data/mock'

export default function XAIPage() {
  const s = mock.xaiExample
  return (
    <div className="space-y-6">
      <div>
        <div className="text-sm uppercase text-slate-300">Explainable AI</div>
        <h1 className="text-3xl font-bold">Explainable AI</h1>
        <p className="text-sm text-slate-300">Understand why the models produce their financial outputs.</p>
      </div>

      <div className="grid lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2 card-glass p-4 rounded-2xl">
          <h3 className="text-sm uppercase text-slate-300">Model Output</h3>
          <div className="mt-4">
            <div className="text-xl font-semibold">{s.stock} — {s.ticker}</div>
            <div className="mt-2">Score: <span className="font-semibold">{s.score}</span> · Risk: <span className="font-semibold">{s.risk}</span></div>
          </div>

          <div className="mt-6">
            <ShapContributionChart contributions={s.contribs} />
          </div>
        </div>

        <div className="card-glass p-4 rounded-2xl">
          <h4 className="text-sm uppercase text-slate-300">Why this result?</h4>
          <p className="mt-3 text-sm text-slate-200">The model attributes positive signal to dividend growth and earnings growth while volatility and payout ratio reduce the score. These explanations are from a demo dataset and are illustrative only.</p>
        </div>
      </div>
    </div>
  )
}
