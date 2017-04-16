console.clear()

import React from 'react';
import ReactDOM from 'react-dom'
import axios from 'axios';
import ReactTable from 'react-table'

class Table extends React.Component {
  constructor(props) {
    super(props);
    this.state = {data: []};
  }

  // Lifecycle method
  componentDidMount (props) {
    // Make HTTP reques with Axios
    axios.get('https://guarded-dawn-62941.herokuapp.com/api/players')
    .then(function (response) {
      this.setState({data:response.data.stats});
    }.bind(this));

  }


  render() {
    var hrdata = this.state.data;
    if (hrdata.length != 0) {

      const columns = [{
        header: 'Name',
        id: 'playerName',
        accessor: hrdata => hrdata.lastname
      },
      {
        header: 'Homeruns',
        id: 'homeruns',
        accessor: hrdata => hrdata.homeruns
      }
    ]

      return (<ReactTable
        showFilters={true}
        data={hrdata}
        columns={columns}/>)

    }
    else { return <div /> }
  }
}


class Table2 extends React.Component {
  constructor(props) {
    super(props);
    this.state = {data: []};
  }

  // Lifecycle method
  componentDidMount (props) {
    // Make HTTP reques with Axios
    axios.get('https://guarded-dawn-62941.herokuapp.com/api/usertotals')
    .then(function (response) {
      this.setState({data:response.data.stats});
    }.bind(this));

  }


  render() {
    var hrdata = this.state.data;
    if (hrdata.length != 0) {

      const columns = [{
        header: 'User',
        id: 'user',
        accessor: hrdata => hrdata.name
      },
      {
        header: 'Homeruns',
        id: 'homeruns',
        accessor: hrdata => hrdata.homeruns
      }
    ]

      return (<ReactTable
        expanderColumnWdith={10}
        showFilters={true}
        data={hrdata}
        columns={columns}/>)


    }
    else { return <div /> }
  }
}

class Table3 extends React.Component {
  constructor(props) {
    super(props);
    this.state = {data: []};
  }

  // Lifecycle method
  componentDidMount (props) {
    // Make HTTP reques with Axios
    axios.get('https://guarded-dawn-62941.herokuapp.com/api/hybrid')
    .then(function (response) {
      this.setState({data:response.data.stats});
    }.bind(this));

  }


  render() {
    var hrdata = this.state.data;
    if (hrdata.length != 0) {

      const columns = [
        {
          header: 'User',
          id: 'user',
          accessor: hrdata => hrdata.name,
          showFilters: true
        },
        {
          header: 'First Name',
          id: 'playerfirstname',
          accessor: hrdata => hrdata.firstname
        },
        {
        header: 'Last Name',
        id: 'playerlastname',
        accessor: hrdata => hrdata.lastname
      },
      {
        header: 'Homeruns',
        id: 'homeruns',
        accessor: hrdata => parseInt(hrdata.homeruns),
        //aggregate: hrdata.map(rows => rows.sum(hrdata.homeruns))
      }
    ]

      return (<ReactTable
        showPagination={false}
        showFilters={true}
        pivotBy={['user']}
        data={hrdata}
        columns={columns}/>)

    }
    else { return <div /> }
  }
}

// conditional rendering based on page
// TODO: figure out a more elegant solution for this
var users = document.getElementById('utab');

if (users) {
  ReactDOM.render(<Table2 />, users);
}

var players = document.getElementById('dtab');

if (players) {
  ReactDOM.render(<Table />, players);
}

var hybrid = document.getElementById('htab');

if (hybrid) {
  ReactDOM.render(<Table3 />, hybrid);
}
