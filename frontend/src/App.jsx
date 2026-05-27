import { useState } from 'react'
import SummaryCards from "./components/SummaryCards"
import TransactionForm from "./components/TransactionForm"
import TransactionList from "./components/TransactionList"

function App() {
  return (
    <div>
      <h1>Student Budget Planner</h1>

      <SummaryCards />
      <TransactionForm />
      <TransactionList />
    </div>
    
  )
}

export default App