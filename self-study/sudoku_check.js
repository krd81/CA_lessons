/*
Check whether a given 9x9 2D array represents a valid Sudoku puzzle.
Return true if the Sudoku puzzle is valid, and false if it is not.
Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-grids of the grid must contain the digits 1-9 without repetition.
*/

const board_1 =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

const board_2 =
[["8","3",".",".","7",".",".","1","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","2",".",".",".",".","6","."]
,["1",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]


function sudokuCheck(board) {
    /*
    1. Check rows (if violation found - mark false)
    2. Check columns
    3. Check 3*3 squares
    */
   let valid = true
    // Check rows
    try {
        for (let n=0; n<board.length; n++){
            let array = board[n]
            checkRows(array)
        }
    } catch (e) {
        console.log('Sudoku board invalid - row(s) contain repeated digits')
    }


    function checkRows (array) {
            // for (let n=0; n<board.length; n++){
                // let array = board[n]
                for (let i=0; i<array.length-1; i++) {
                    for (let j=i+1; j<array.length; j++) {
                        if (array[i] !== '.' && array[j] !== '.') {
                            if (array[i] === array[j]) {
                                valid = false
                                throw new Error('Invalid Sudoku')
                            }
                        }
                    }
                } return valid
            // }
    }



    // Check columns
    if (valid) {
        try {
            // Array 0, element 0 compared to
            // -- Array 1, element 0
            // -- Array 2, element 0
            // -- Array 3, element 0
            for (let element=0; element<9; element++){
                for (let i=0; i<board.length-1; i++) {
                    let firstArray = board[i]
                    for (let j=i+1; j<board.length; j++) {
                        let secondArray = board[j]
                        if (firstArray[element] !== '.' && secondArray[element] !== '.') {
                            if (firstArray[element] === secondArray[element]) {
                                valid = false
                                throw new Error('Invalid Sudoku')
                            }
                        }
                    }
                }
            }
        } catch (e) {
            console.log('Sudoku board invalid - column(s) contain repeated digits')
        }
    }

    // Check 3x3 squares
    // Compare elements 0,1,2 of Arrays 0,1,2 / 3,4,5 / 6,7,8
    // Compare elements 3,4,5 of Arrays 0,1,2 / 3,4,5 / 6,7,8
    // Compare elements 6,7,8 of Arrays 0,1,2 / 3,4,5 / 6,7,8
    if (valid) {
        const array1 = [0, 1, 2]
        const array2 = [3, 4, 5]
        const array3 = [6, 7, 8]

        // Need to iterate through each group for arrays/elements
        checkSquare(array1, array1) // 1
        checkSquare(array1, array2) // 2
        checkSquare(array1, array3) // 3
        checkSquare(array2, array1) // 4
        checkSquare(array2, array2) // 5
        checkSquare(array2, array3) // 6
        checkSquare(array3, array1) // 7
        checkSquare(array3, array2) // 8
        checkSquare(array3, array3) // 9

    }


    function checkSquare (elements, arrays) {
        let square = []
        // elements = [0,1,2] arrays[3,4,5]
        for (let i in arrays) {
            let array = board[arrays[i]]
            for (let j of elements) {
                square.push(array[j])
            }
        }
        try {
            if (checkRows(square) === true) {
                valid = true
            } else {
                valid = false
            }
        } catch (e) {
            console.log('Sudoku board invalid - 3x3 square(s) contain repeated digits')
        }


}



if (valid) {
    console.log('Sudoku board is valid')
}




}



sudokuCheck(board_1)
sudokuCheck(board_2)

