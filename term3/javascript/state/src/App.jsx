import React, { useState } from 'react'
import BitcoinIndex from './BitcoinIndex'

const App = () => {
  return (
    <>
    <h1>Bitcoin Index...</h1>
    <BitcoinIndex currency="EUR" />
    </>
  )
}

export default App