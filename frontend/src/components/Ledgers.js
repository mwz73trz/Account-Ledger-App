import { Component } from "react";
// import { Link } from "react-router-dom";

class Ledgers extends Component {
  render() {
    return (
      <tr>
        <td>{this.props.ledger.type}</td>
        <td>{this.props.ledger.check_number}</td>
        <td>{this.props.ledger.date}</td>
        <td>{this.props.ledger.description}</td>
        <td>{this.props.ledger.deposit_amount}</td>
        <td>{this.props.ledger.withdrawal_amount}</td>
        <td>{this.props.ledger.balance.balance}</td>
      </tr>
    );
  }
}

export default Ledgers;
