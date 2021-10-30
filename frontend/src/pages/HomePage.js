import { Component } from "react";
import Ledgers from "../components/Ledgers";
import accountLedgerAPI from "../api/accountLedgerAPI";

class HomePage extends Component {
  state = {
    ledgers: [],
  };

  getLedgers = async () => {
    try {
      let ledgersData = await accountLedgerAPI.getLedgers();
      this.setState({ ledgers: ledgersData });
    } catch (error) {
      console.log(error);
    }
  };

  componentDidMount() {
    this.getLedgers();
  }

  renderWelcome() {
    let ledgerElements = this.state.ledgers.map((ledger, index) => {
      return (
        <tbody key={`ledger-${index}`}>
          <Ledgers ledger={ledger} />
        </tbody>
      );
    });
    return (
      <div>
        <h2>Welcome to your Account Management App</h2>
        <h2>Ledger</h2>
        <table border="1">
          <thead>
            <tr>
              <th>Type</th>
              <th>Check Number</th>
              <th>Date</th>
              <th>Description</th>
              <th>Deposit Amount</th>
              <th>Withdrawal Amount</th>
              <th>Balance</th>
            </tr>
          </thead>
          {ledgerElements}
        </table>
      </div>
    );
  }

  render() {
    return (
      <div>
        <h1>Home Page</h1>
        {this.renderWelcome()}
      </div>
    );
  }
}

export default HomePage;
