const LABELS = [1, 2, 3, 4, 5, 6, 7, 8, 9] as const;
type Label = typeof LABELS[number];

type Line<T> = [T, T, T, T, T, T, T, T, T];
type Grid<T> = Line<Line<T>>;

class Sudoku {
    public grid: Grid<Label | null>;
    public possibilities: Grid<Label[]>;

    constructor(input: Grid<Label | null>) {
        this.grid = input;

        this.possibilities = input.map(line =>
            line.map(element =>
                (element !== null) ? [element] : [1, 2, 3, 4, 5, 6, 7, 8, 9]
            )
        ) as Grid<Label[]>;
    }

    public solve() {
        this.grid.forEach((row, i) => row.forEach((element, j) => {
            if (element !== null)
                this.filterNeighbors(i, j, element);
        }));
    }


    public filterNeighbors(i: number, j: number, value: Label) {

    }

    private filterSquare(i: number, j: number, value: Label) {
        this.grid[i][j]
    }

    private filterColumn(i: number, value: Label) {
        const x = this.possibilities[i].map(e =>
            e.filter(possibility => possibility !== value)
        );
        this.possibilities[i].forEach(arr => {
            arr.splice(arr.findIndex(label => label === value), 1);
        })
    }

    private filterRow(j: number, value: Label) {
        this.grid[i][j]
    }
}
