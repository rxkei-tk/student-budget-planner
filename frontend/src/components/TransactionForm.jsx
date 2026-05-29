import { useState } from "react"

function TransactionForm() {
    const [formData, setFormData] = useState({
        type: "expense",
        name: "",
        category: "",
        amount: "",
        date: ""
    })

    function handleChange(event) {
        const { name, value } = event.target

        setFormData({
            ...formData,
            [name]: value
        })
    }

    function handleSubmit(event) {
        event.preventDefault()
        console.log(formData)

        setFormData({
            type: "expense",
            name: "",
            category: "",
            amount: "",
            date: ""
        })
    }

    return ( 
        <form onSubmit={handleSubmit}>
            <h2>Transaction Form</h2>

            <div>
                <h3>Type:</h3>
                <select
                    name="type"
                    value={formData.type}
                    onChange={handleChange}
                >
                    <option value="income">Income</option>
                    <option value="expense">Expense</option>
                </select>
            </div>
            <div>
                <h3>Name:</h3>
                <input
                    type="text"
                    name="name"
                    value={formData.name}
                    onChange={handleChange}
                />
            </div>
            <div>
                <h3>Category:</h3>
                <input
                    type="text"
                    name="category"
                    value={formData.category}
                    onChange={handleChange}
                />
            </div>
            <div>
                <h3>Amount:</h3>
                <input
                    type="number"
                    name="amount"
                    value={formData.amount}
                    onChange={handleChange}
                />
            </div>
            <div>
                <h3>Date:</h3>
                <input
                    type="date"
                    name="date"
                    value={formData.date}
                    onChange={handleChange}
                />
            </div>
            <div>
                <button type="submit" style={{marginTop: "20px"}}>
                    Save Workout
                </button>
            </div>
        </form>
    )
}

export default TransactionForm