"""Dictionary related utility functions."""

__author__ = "730307805"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a cvs into a 'table'."""
    result: list[dict[str, str]] = []
    
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CVS line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()
    return result


# In the notebook, the function call won't work when I change the colum from date
def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform  a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result 


def head(table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Produce a column-based table with only the first N rows of data."""
    result: dict[str, list[str]] = {}

    return result