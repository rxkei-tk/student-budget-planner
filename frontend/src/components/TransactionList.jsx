function TransactionList({ transactions }) {
    

    if (transactions.length === 0) {
        return <p>No transactions yet</p>
    }

    return (
    <div>
        <h2>Transaction List</h2>
        <p>-------------------------------------</p>

        {transactions.map((transaction, index) => (
            <div key={index}>
                <p> Type: {transaction.type}</p>
                <p> Name: {transaction.name}</p>
                <p> Category: {transaction.category}</p>
                <p> Amount: ${transaction.amount}</p>
                <p> Date: {transaction.date}</p>
                <p>-------------------------------------</p>
            </div>
        ))} 
    </div>
    )
}

export default TransactionList