import React, { useState, useEffect } from 'react'

// const CurrencySelector = ({ currency, setCurrency }) => {
// if using this option, 
const CurrencySelector = ({ setCurrency }) => {
    // This state is the single source of truth
    const [currencies, setCurrencies] = useState([])
    const [selectValue, setSelectValue] = useState("AUD")
    useEffect(() => setCurrency(selectValue), [selectValue])

    useEffect(() => {
        fetch('https://api.coindesk.com/v1/bpi/supported-currencies.json')
        .then(res => res.json())
        .then(data => setCurrencies(data))
    }, [])

  return (
    // This select box is a controlled element, as its value is being controlled by the state
    // It has two-way binding as the state gets the value from the element or vice versa
    // <select name="" id="currency-selector">
    <select onChange={event => setSelectValue(event.target.value)} value={selectValue}>
        {/* <option value="AUD">Australian Dollar</option>
        <option value="USD">US Dollar</option>
        <option value="EUR">Euro</option> */}
        {currencies.map(cur => <option value={cur.currency}>{cur.country}</option>)}
    </select>
  )
}

export default CurrencySelector

// This is how we would access the value a user selected using plain JavaScript
// const select = document.querySelector('#currency-selector')
// select.value