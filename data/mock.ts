import { Stock, Summary, Portfolio, FeatureImportance, ShapContribution } from '../types'

export const mock = {
  topStock: { ticker: 'ABC', company: 'Alpha Beta Co.' },
  summary: { avgDividendYield: 3.2, marketCoverage: 35, sectorsCovered: 6 } as Summary,
  stocks: [
    { rank: 1, ticker: 'ABC', company: 'Alpha Beta Co.', sector: 'Industrials', dividendYield: 4.2, dividendScore: 92, payoutRatio: 45, risk: 'Low', signal: 'Buy' },
    { rank: 2, ticker: 'DEF', company: 'Delta Echo', sector: 'Utilities', dividendYield: 3.8, dividendScore: 88, payoutRatio: 60, risk: 'Medium', signal: 'Hold' },
    { rank: 3, ticker: 'GHI', company: 'Gamma Holdings', sector: 'Financials', dividendYield: 2.5, dividendScore: 76, payoutRatio: 35, risk: 'High', signal: 'Watch' }
  ] as Stock[],
  sectorMix: [
    { name: 'Industrials', value: 32 },
    { name: 'Utilities', value: 24 },
    { name: 'Financials', value: 18 },
    { name: 'Technology', value: 15 },
    { name: 'Healthcare', value: 11 }
  ],
  signals: [
    { title: 'High Dividend Stability', desc: 'Dividend payments stable over past 8 years.' },
    { title: 'Earnings Momentum', desc: 'Positive earnings revisions in latest quarter.' }
  ],
  portfolio: { yield: 3.6, volatility: 8.2 } as Portfolio,
  riskDistribution: { low: '45%', medium: '35%', high: '20%' },
  featureImportance: { rf: [ { name: 'Dividend Yield', value: 0.42 }, { name: 'Payout Ratio', value: 0.28 }, { name: 'Earnings Growth', value: 0.18 } ], xgb: [ { name: 'Dividend Yield', value: 0.38 }, { name: 'Earnings Growth', value: 0.24 }, { name: 'Volatility', value: 0.12 } ] } as FeatureImportance,
  xaiExample: {
    stock: 'Alpha Beta Co.',
    ticker: 'ABC',
    score: 0.78,
    risk: 'Low',
    contribs: [
      { feature: 'Dividend Growth', value: 0.31 },
      { feature: 'Earnings Growth', value: 0.24 },
      { feature: 'Yield Stability', value: 0.18 },
      { feature: 'Payout Ratio', value: -0.09 },
      { feature: 'Volatility', value: -0.14 }
    ] as ShapContribution[]
  }
}
