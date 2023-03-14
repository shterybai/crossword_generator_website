// const crosswordContainer = document.getElementById('crossword');
// const crosswordGrid = document.getElementById('grid');
// crosswordGrid.classList.add('crossword-grid');
// crosswordContainer.appendChild(crosswordGrid);
//
// for (let row = 1; row <= numRows; row++) {
//
// }

const acrossClues = document.getElementById('across_clues');
const downClues = document.getElementById('down_clues');

const numAcrossClues = 8;
const acrossNums = [6, 7, 8, 9, 11, 12, 15, 16]

const numDownClues = 9;
const downNums = [1, 2, 3, 4, 5, 10, 11, 13, 14]

fetch('/fyp')
    .then((response) => response.json())
    .then((data) => {
        console.log(data)
    })
    .catch(error => {
        console.error(error)
    });
    // .then((res)=>{ console.log(res) })

for (let i = 0; i < numAcrossClues; i++) {
    var li = document.createElement("li")

    var text = document.createTextNode(acrossNums[i] + ": " + ['{{ clue[i] }}'])
    li.appendChild(text)

    acrossClues.appendChild(li)
}

for (let i = 0; i < numDownClues; i++) {
    var li = document.createElement("li")

    var text = document.createTextNode(downNums[i] + ": " + ['{{ clue[i] }}'])
    li.appendChild(text)

    downClues.appendChild(li)
}

