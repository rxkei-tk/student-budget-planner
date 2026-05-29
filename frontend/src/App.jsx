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

  async function createTransaction(transaction) {
    const response = await fetch("http://127.0.0.1:5050/transactions", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(transaction),
    })

    const data = await response.json()
    console.log(data)

    fetchTransactions()
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
        <TransactionForm onAddTransaction={createTransaction} />
      </section>

      <section>
        <TransactionList transactions={transactions} />
      </section>
    </main>    
  )
}

export default App