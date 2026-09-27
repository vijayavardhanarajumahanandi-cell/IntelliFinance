import FeatureImportanceChart from '../../components/FeatureImportanceChart'
import { mock } from '../../data/mock'

export default function MLDriversPage() {
  return (
    <div className="space-y-6">
      <div>
        <div className="text-sm uppercase text-slate-300">Model Drivers</div>
        <h1 className="text-3xl font-bold">Model Drivers</h1>
        <p className="text-sm text-slate-300">Compare the features driving Random Forest and XGBoost financial analysis.</p>
      </div>

      <div className="card-glass p-4 rounded-2xl">
        <FeatureImportanceChart rf={mock.featureImportance.rf} xgb={mock.featureImportance.xgb} />
      </div>

      <div className="grid md:grid-cols-2 gap-4">
        <div className="card-glass p-4 rounded-2xl">
          <h3 className="text-sm uppercase text-slate-300">Random Forest</h3>
          <div className="mt-3 text-sm text-slate-200">Robust to noise, interpretable via aggregated feature importance.</div>
        </div>
        <div className="card-glass p-4 rounded-2xl">
          <h3 className="text-sm uppercase text-slate-300">XGBoost</h3>
          <div className="mt-3 text-sm text-slate-200">High-performing gradient boosting with regularization and feature importance.</div>
        </div>
      </div>
    </div>
  )
}
