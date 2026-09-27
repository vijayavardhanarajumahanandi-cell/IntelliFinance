import Link from 'next/link'
import Hero from '../components/Hero'
import FeatureCard from '../components/FeatureCard'
import { BankNote, ShieldCheck, Cpu, Eye } from 'lucide-react'

export default function Home() {
  return (
    <div className="space-y-10">
      <Hero />

      <section className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <FeatureCard title="Financial Intelligence" icon={<BankNote />} description="Deep fundamental analytics and dividend research." />
        <FeatureCard title="Risk Analytics" icon={<ShieldCheck />} description="Portfolio risk, drawdown analysis, and scenario testing." />
        <FeatureCard title="Machine Learning" icon={<Cpu />} description="Multi-model analysis: Random Forest, XGBoost, clustering." />
        <FeatureCard title="Explainable AI" icon={<Eye />} description="SHAP explanations and model interpretability." />
      </section>

      <section className="grid lg:grid-cols-2 gap-8">
        <div className="card-glass p-6 rounded-2xl">
          <h3 className="text-sm uppercase text-slate-300 tracking-widest">Research Pipeline</h3>
          <div className="mt-6">
            <ol className="space-y-4">
              <li>Financial Data → Feature Engineering → Financial Analytics → Machine Learning → Explainable AI → Risk & Portfolio Analytics</li>
            </ol>
          </div>
        </div>

        <div className="card-glass p-6 rounded-2xl">
          <h3 className="text-sm uppercase text-slate-300 tracking-widest">Model Intelligence</h3>
          <ul className="mt-4 space-y-3 text-sm text-slate-200">
            <li><strong>K-Means</strong> — Uncovers clusters in financial behavior.</li>
            <li><strong>Random Forest</strong> — Robust feature importance for structured data.</li>
            <li><strong>XGBoost</strong> — High-performance gradient boosting for ranking.</li>
            <li><strong>SHAP</strong> — Local explanations to attribute predictions to features.</li>
          </ul>
        </div>
      </section>

      <section className="grid lg:grid-cols-3 gap-6">
        <div className="card-glass p-6 rounded-2xl">
          <h4 className="text-xs uppercase text-slate-300">Top Ranked Stocks</h4>
          <p className="mt-4 text-2xl font-semibold">Demo dataset: Top picks across quality and yield</p>
        </div>
        <div className="card-glass p-6 rounded-2xl">
          <h4 className="text-xs uppercase text-slate-300">Sector Mix</h4>
        </div>
        <div className="card-glass p-6 rounded-2xl">
          <h4 className="text-xs uppercase text-slate-300">Feature Importance</h4>
        </div>
      </section>

      <section className="text-center py-12">
        <h2 className="text-2xl font-bold">Turn fragmented financial data into interpretable intelligence.</h2>
        <div className="mt-6 flex justify-center gap-4">
          <Link href="/dashboard" className="px-6 py-3 rounded-xl bg-accent text-black font-semibold">Open Dashboard</Link>
          <Link href="/dashboard" className="px-6 py-3 rounded-xl border border-white/10">View Research</Link>
        </div>
      </section>

      <footer className="p-6 text-sm text-slate-400">
        <div className="max-w-4xl mx-auto flex justify-between">
          <div>
            <div className="font-semibold">IntelliFinance</div>
            <div className="mt-2">Research-oriented financial analytics platform.</div>
          </div>
          <div className="flex gap-4">
            <Link href="/dashboard">Dashboard</Link>
            <Link href="/risk">Risk</Link>
            <Link href="/ml-drivers">ML Drivers</Link>
            <Link href="/xai">XAI</Link>
            <a href="https://github.com/vijayavardhanarajumahanandi-cell/IntelliFinance" target="_blank" rel="noreferrer">GitHub</a>
          </div>
        </div>
      </footer>
    </div>
  )
}
