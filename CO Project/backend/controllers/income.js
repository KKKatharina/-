

exports.addIncome = async (req, res) =>
{
    const {title, amount, category, description, date} = req.body

    const income = IncomeSchema({
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
        await income.save()
        res.status(200).json({message: "Income Added Successfully"})
        console.log(income)
    } 
    catch(error)
    {
        res.status(500).json({message: "Server Error"})
    }
}

exports.getIncome = async (req, res) => 
{
        const {id} = req.params;
        console.log(id);
}