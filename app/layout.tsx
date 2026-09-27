import './globals.css'
import { ReactNode } from 'react'
import Sidebar from '../components/Sidebar'
import Navbar from '../components/Navbar'

export const metadata = {
  title: 'IntelliFinance',
  description: 'Integrated ML financial analytics and research platform.'
}

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body>
        <div className="app-shell">
          <Sidebar />
          <div className="flex-1 flex flex-col min-h-screen">
            <Navbar />
            <main className="main-content">{children}</main>
          </div>
        </div>
      </body>
    </html>
  )
}
