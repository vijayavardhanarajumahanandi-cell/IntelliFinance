export type Stock = {
  rank: number
  ticker: string
  company: string
  sector: string
  dividendYield: number
  dividendScore: number
  payoutRatio: number
  risk: 'Low' | 'Medium' | 'High'
  signal: string
}

export type Summary = {
  avgDividendYield: number
  marketCoverage: number
  sectorsCovered: number
}

export type Portfolio = {
  yield: number
  volatility: number
}

export type FeatureImportance = {
  rf: { name: string; value: number }[]
  xgb: { name: string; value: number }[]
}

export type ShapContribution = {
  feature: string
  value: number
}
