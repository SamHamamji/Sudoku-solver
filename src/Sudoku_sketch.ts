// const LABELS = [1, 2, 3, 4, 5, 6, 7, 8, 9] as const;
// type Label = typeof LABELS[number];

// type Line<T> = [T, T, T, T, T, T, T, T, T];
// type Grid<T> = Line<Line<T>>;

// class Sudoku {
//     public grid: Grid<Label[] | Label>;

//     constructor(input: Grid<Label | null>) {
//         this.grid = input.map(
//             line => line.map(element => element ?? LABELS)
//         ) as Grid<Label | Label[]>;
//     }

//     public solve() {

//     }

//     public filterNeighbors(i, j, value) {

//     }

//     private filterSquare(i, j, value) {
//         this.grid[i][j]
//     }

//     private filterColumn(i: number, value: Label) {
//         this.grid[i] = this.grid[i].map(e => {
//             if (e instanceof Array)
//                 return e.filter(possibility => possibility !== value)
//             return e;
//         })
//     }

//     private filterRow(j, value: Label) {
//         this.grid[i][j]
//     }
// }
