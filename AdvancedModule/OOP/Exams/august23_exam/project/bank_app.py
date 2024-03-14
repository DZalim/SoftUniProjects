from typing import List

from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:

    VALID_LOANS = {
        'StudentLoan': StudentLoan,
        'MortgageLoan': MortgageLoan
    }

    VALID_CLIENTS = {
        'Student': Student,
        'Adult': Adult
    }

    VALID_COMBINATIONS = {
        'StudentLoan': 'Student',
        'MortgageLoan': 'Adult'
    }

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.VALID_LOANS:
            raise Exception("Invalid loan type!")

        current_loan = self.VALID_LOANS[loan_type]()
        self.loans.append(current_loan)

        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_CLIENTS:
            raise Exception("Invalid client type!")

        if len(self.clients) == self.capacity:
            return "Not enough bank capacity."

        current_client = self.VALID_CLIENTS[client_type](client_name, client_id, income)
        self.clients.append(current_client)
        
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        current_client = self.get_client(client_id)
        client_type = current_client.__class__.__name__
        current_loan = self.get_loan(loan_type)

        if client_type != self.VALID_COMBINATIONS[loan_type]:
            raise Exception("Inappropriate loan type!")

        self.loans.remove(current_loan)
        current_client.loans.append(current_loan)

        return f"Successfully granted {loan_type} to {current_client.name} with ID {client_id}."

    def remove_client(self, client_id: str):

        current_client = self.get_client(client_id)

        if not current_client:
            raise Exception("No such client!")

        if current_client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(current_client)
        return f"Successfully removed {current_client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        loans_to_increase = [loan.increase_interest_rate()
                             for loan in self.loans if loan.__class__.__name__ == loan_type]

        return f"Successfully changed {len(loans_to_increase)} loans."

    def increase_clients_interest(self, min_rate: float):

        loans_to_increase = [client.increase_clients_interest()
                             for client in self.clients if client.interest < min_rate]

        return f"Number of clients affected: {len(loans_to_increase)}."

    def get_statistics(self):
        total_clients_income = sum([client.income for client in self.clients])
        loans_count_granted_to_clients = sum([len(loan.loans) for loan in self.clients])
        granted_sum = sum([amount.amount for loan in self.clients for amount in loan.loans])
        loans_count_not_granted = len([loan for loan in self.loans])
        not_granted_sum = sum([loan.amount for loan in self.loans])

        try:
            avg_client_interest_rate = sum([client.interest for client in self.clients]) / len(self.clients)
        except ZeroDivisionError:
            avg_client_interest_rate = 0

        return (f"Active Clients: {len(self.clients)}\n"
                f"Total Income: {total_clients_income:.2f}\n"
                f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}\n"
                f"Available Loans: {loans_count_not_granted}, Total Sum: {not_granted_sum:.2f}\n"
                f"Average Client Interest Rate: {avg_client_interest_rate:.2f}")

    def get_client(self, client_id):
        client = [client for client in self.clients if client_id == client.client_id]
        return client[0] if client else None

    def get_loan(self, loan_type):
        loan = [loan for loan in self.loans if loan_type == loan.__class__.__name__]
        return loan[0] if loan else None
