import React, {useEffect} from 'react';
import { makeStyles, withStyles, InputLabel, MenuItem, FormControl, Select, Button,
  Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, Typography, } from '@material-ui/core';

const useStyles = makeStyles((theme) => ({
  formControl: {
    margin: theme.spacing(1),
    minWidth: 120,
  },

  table: {
    minWidth: 700,
  },
}));

const StyledTableCell = withStyles((theme) => ({
  head: {
    backgroundColor: theme.palette.primary.dark,
    color: theme.palette.common.white,
  },
  body: {
    fontSize: 14,
  },
}))(TableCell);

const StyledTableRow = withStyles((theme) => ({
  root: {
    '&:nth-of-type(odd)': {
      backgroundColor: theme.palette.action.hover,
    },
  },
}))(TableRow);

function createData(name, lastName) {
  return { name, lastName };
}

const WorkerList = () => {
  const classes = useStyles();
  const [book, setBook] = React.useState('');
  const [rowsBook, set_rowsBook] = React.useState([]);
  const [rowsWorkers, set_rowsWorkers] = React.useState([]);
  const handleChange = (event) => {
    setBook(event.target.value);
  };

  useEffect(async () => {
    const response = await fetch('http://localhost:4000/Books', {
      method: 'GET',
      headers : {
        Accept: '*/*',
        'Content-Type': 'text/plain',
        user: localStorage.getItem("account")
      },
    });
    const json = await response.json();
    set_rowsBook(json);
  }, []);

  const handleOpen = async () => {
    let test = await fetch('http://localhost:4000/Workers', {
      method: 'GET',
      headers : {
        Accept: '*/*',
        'Content-Type': 'text/plain',
        documentName: book
      },
    });
    const json = await test.json();   
    set_rowsWorkers(json);
  };

  return (
    <div>
      <Typography variant="h6" color="initial"> Select the book's name for  consult:</Typography>
      <FormControl className={classes.formControl}>
        <InputLabel>Book name</InputLabel>
        <Select
          value={book}
          onChange={handleChange}
        >
          {rowsBook.map((rowBook) => (
          <MenuItem value={rowBook.name}>{rowBook.name}</MenuItem>
          ))}
        </Select>
      </FormControl>
      <p></p>
      <Button variant="contained" color="primary" onClick={handleOpen}>
        Accept
      </Button>
      <p></p>
      <TableContainer component={Paper}>
        <Table className={classes.table} aria-label="customized table">
          <TableHead>
            <TableRow>
              <StyledTableCell>Name</StyledTableCell>
              <StyledTableCell >Last Name</StyledTableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {rowsWorkers.map((row) => (
              <StyledTableRow key={row.name}>
                <StyledTableCell component="th" scope="row">
                  {row.name}
                </StyledTableCell>
                <StyledTableCell>{row.lastName}</StyledTableCell>
              </StyledTableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </div>
  );
}

export default WorkerList;
