import { useState, useEffect } from "react"
import SummaryCards from "./components/SummaryCards"
import TransactionForm from "./components/TransactionForm"
import TransactionList from "./components/TransactionList"

function App() {
  const [transactions, setTransactions] = useState([])

  async function fetchTransactions() {
    const response = await fetch("http://127.0.0.1:5050/transactions")
    const data = await response.json()
    setTransactions(data)

  }

  function addTransaction(transaction) {
    setTransactions([...transactions, transaction])
  }

  useEffect(() => {
    fetchTransactions()
  }, [])

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