FILENAME = "puzzle1.grd"


class Grid(object):
    """
        TODO:
            - Interface
            - File export
            - Column and row headers
            - Dividers
    """

    def __init__(self, 
                 input_str='100\n010\n001', 
                 empty_val='0', 
                 empty_mask='.', 
                 extend=False):

        """
            Loads *.grid file into self._grid as 9x9 2d python list
        """

        self._empty_val = empty_val
        self._empty_mask = empty_mask
        self._grid = self._read_to_grid(input_str)

    def __str__(self, row_column_labels=False):
        row_len = max(len(row) for row in self._grid)
        lines = [f"+{'---' * row_len}+", ]

        # Row, row, row your strings
        for row in self._grid:
            lines += [f"|{''.join(f' {cell} ' for cell in row)}|"
                          .replace(self._empty_val, self._empty_mask)]

        # User header as footer
        lines.append(lines[0])

        # happy string
        return "".join(line + '\n' for line in lines)

    @staticmethod
    def _read_to_grid(input_str: str, extend=False) -> list:
        """
            Attempts to read lines from input string as either:

              - a *.grd file
              - a newline delimited string

            Each row becomes a list of single character non-whitespace strings.
            The return is a simple 2d list.
        """

        # If input is a *.grd file
        if input_str.split(sep='.')[-1] == 'grd':
            with open(input_str, 'r') as file_obj:
                input_str = "".join(file_obj.readlines())
        
        # self._grid data as 2d list
        return [list(line) for line in input_str.split()]

    def set_empty_mask(self, mask="."):
        self._empty_mask = mask
        return self

    def set_value(self, row, col, value):
        self._grid[row][col] = value 

    def get_value(self, row, col):
        return self._grid[row][col]


def main():
    # Basic, all defaults at creation
    grid_zero = Grid(FILENAME)
    print(grid_zero)
    print(grid_zero.get_value(0, 0))

    grid_zero.set_value(0, 0, "1")
    print(grid_zero.get_value(0, 0))
    print(grid_zero)

    # grid_zero.set_value(8, 8, "2")
    # print(grid_zero)
    # grid_zero.get_value(0, 0)

    # # Construction using filename
    # grid_foreign = Grid(FILENAME)
    # print(grid_foreign)
    # print(grid_foreign.set_empty_mask(' '))

    # # Using string input
    # grid_domestic = Grid("xoxo\noxox\nxoxo\noxox")
    # print(grid_domestic)
    # print(grid_domestic.set_empty_mask('x'))


if __name__ == '__main__':
    main()
