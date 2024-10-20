<template>

  <div class="sudoku-container">
    <div v-for="(block, blockIndex) in 9" :key="blockIndex" class="sudoku-block">
      <button 
      v-for="(cell, cellIndex) in 9" 
      :key="cellIndex" 
      class="cell"
      @click="selectCell(Math.floor(blockIndex / 3) * 3 + Math.floor(cellIndex / 3), (blockIndex % 3) * 3 + (cellIndex % 3))">
        {{sudoku[Math.floor(blockIndex / 3) * 3 + Math.floor(cellIndex / 3)][(blockIndex % 3) * 3 + cellIndex % 3] || ''}}
      </button>
    </div>
  </div>
  <button @click="solveSudoku">Solve Sudoku</button>
</template>
<script>
export default {
    name: 'GridSudoku',
  data() {
    return {
      sudoku: [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
      ]
    };
  },
 methods: {
    async solveSudoku() {
      try{
        const response = await fetch('http://127.0.0.1:5000/solve', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ board: this.sudoku })
        });

        if(!response.ok){
          throw new Error('Network respone was not ok')
        }
        const solvedBoard = await response.json();
        console.log("Updated Sudoku: ", solvedBoard);
        this.sudoku = solvedBoard;
      } catch (error){
        console.error('Error during fetch:', error)
      }
    },

    selectCell(rowIndex, colIndex) {
        const newValue = prompt("number between (1-9):");
        if (newValue >= 0 && newValue <= 9) {
            this.sudoku[rowIndex][colIndex] = parseInt(newValue);
        }
    }
 }
 };
</script>

<style scoped>

.sudoku-container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-template-rows: repeat(3, 1fr);
    margin: 0px;
    width: 500px;
    height: 500px;
    border: 2px solid;
}


.sudoku-block {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-template-rows: repeat(3, 1fr);
    border: 2px solid;
}

.cell{
  border: 1px solid;
  font-size: 30px;
  text-align: center;
}
</style>