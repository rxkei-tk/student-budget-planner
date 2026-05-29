import { useState } from 'react'
import SummaryCards from "./components/SummaryCards"
import TransactionForm from "./components/TransactionForm"
import TransactionList from "./components/TransactionList"

function App() {
  return (
    <main>
      <h1>Student Budget Planner</h1>

      <section>
        <SummaryCards />
      </section>

      <section>
        <TransactionForm />
      </section>

      <section>
        <TransactionList />
      </section>
    </main>    
  )
}

export default App