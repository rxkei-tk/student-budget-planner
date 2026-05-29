import { useState } from 'react'
import SummaryCards from "./components/SummaryCards"
import TransactionForm from "./components/TransactionForm"
import TransactionList from "./components/TransactionList"

function App() {
  const [transactions, setTransactions] = useState([])

  function addTransaction(transaction) {
    setTransactions([...transactions, transaction])
  }

  return (
    <main>
      <h1>Student Budget Planner</h1>

      <section>
        <SummaryCards />
      </section>

      <section>
        <TransactionForm onAddTransaction={addTransaction} />
      </section>

      <section>
        <TransactionList transactions={transactions} />
      </section>
    </main>    
  )
}

export default App