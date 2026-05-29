function TransactionForm() {
    return ( 
    <div>
        <h2>Transaction Form</h2>

        <div>
            <h3>Type:</h3>
            <select name="Type">
                <option value="income">Income</option>
                <option value="expense">Expense</option>
            </select>
        </div>
        <div>
            <h3>Name:</h3>
            <input type="text" placeholder="Name" />
        </div>
        <div>
            <h3>Category:</h3>
            <input type="text" placeholder="Category" />
        </div>
        <div>
            <h3>Amount:</h3>
            <input type="number" placeholder="Amount" />
        </div>
        <div>
            <h3>Date:</h3>
            <input type="date"/>
        </div>
    </div>
    )
}

export default TransactionForm