

exports.addExpense = async (req, res) =>
    {
        const {title, amount, category, description, date} = req.body
    
        const expense = ExpenseSchema({
            title,
            amount,
            category,
            description,
            date,
        })
        try 
        {
            //validations
            if(!title || !amount || !category || !description || !date)
            {
                return res.status(400).json({message: "Please fill all the fields"})
            }
            if(amount <= 0|| !amount === 'number') 
            {
                return res.status(400).json({message: "Amount should be greater than 0"})
            }
            await expense.save()
            res.status(200).json({message: "Expense Added Successfully"})
            console.log(expense)
        } 
        catch(error)
        {
            res.status(500).json({message: "Server Error"})
        }
    }
    
    exports.getExpense = async (req, res) => 
    {
            const {id} = req.params;
            console.log(id);
    }