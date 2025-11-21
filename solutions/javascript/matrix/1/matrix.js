//
// This is only a SKELETON file for the 'Matrix' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export class Matrix {
  constructor(data) {
    this._rows = [];
    this._columns = [];

    let rows = data.split("\n");
    
    for (let idx_row = 0; idx_row < rows.length; idx_row++) {
      let colums = rows[idx_row].split(" ");

      while (this._columns.length < colums.length) {
        this._columns.push([]);
      }

      let temp_row = [];

      for (let idx_column = 0; idx_column < colums.length; idx_column++) {
        temp_row.push(Number(colums[idx_column]));
        this._columns[idx_column].push(Number(colums[idx_column]));
      }
      this._rows.push(temp_row);
    }
  }

  get rows() {
    return this._rows;
  }

  get columns() {
    return this._columns;
  }
}
