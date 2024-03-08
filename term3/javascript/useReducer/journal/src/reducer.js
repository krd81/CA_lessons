import  createContext  from 'react'

// the action is an action that a component wants to perform on the state
// not a user action (like onClick)
export default function reducer(state, action) {
    // console.log(state)
    // console.log(action)
    switch(action.type){
      case 'set categories':
        return { 
          ...state, 
          categories: action.data
        }
      case 'set entries':
        return {
        ...state, 
        entries: action.data
    }
        case 'add entry':
          return {
            ...state, 
            entries: [...state, action.data]
    }
  }
  }

// a context is a way to share data between components without having to pass it down through props
// it is like a container for a value
export const journalContext = createContext()

