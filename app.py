import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.candidates import create_candidate, get_candidates, update_candidate, delete_candidate
from models.voter import create_voter, get_voters, update_voter, delete_voter
from models.vote import create_vote, get_votes, view_results
from database.db_setup import init_db

# Welcome message
def welcome():
    print("Welcome to the Online Voting System")

# Main menu options
def show_menu():
    print("\nChoose an option:")
    print("1. Manage Candidates")
    print("2. Manage Voters")
    print("3. Manage Votes")
    print("4. View Voting Results")
    print("5. Exit")

# Manage Candidates submenu
def manage_candidates():
    while True:
        print("\nManage Candidates:")
        print("1. Add Candidate")
        print("2. View Candidates")
        print("3. Update Candidate")
        print("4. Delete Candidate")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter candidate's name: ")
            party = input("Enter candidate's party: ")
            create_candidate(name, party)
        elif choice == '2':
            get_candidates()  
        elif choice == '3':
            candidate_id = int(input("Enter candidate ID to update: "))
            name = input("Enter new name (leave blank to keep current): ")
            party = input("Enter new party (leave blank to keep current): ")
            update_candidate(candidate_id, name, party)
        elif choice == '4':
            candidate_id = int(input("Enter candidate ID to delete: "))
            delete_candidate(candidate_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

# Manage Voters submenu
def manage_voters():
    while True:
        print("\nManage Voters:")
        print("1. Add Voter")
        print("2. View Voters")
        print("3. Update Voter")
        print("4. Delete Voter")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter voter's name: ")
            age = int(input("Enter voter's age: "))
            create_voter(name, age)
        elif choice == '2':
            get_voters()
        elif choice == '3':
            voter_id = int(input("Enter voter ID to update: "))
            name = input("Enter new name (leave blank to keep current): ")
            age = input("Enter new age (leave blank to keep current): ")
            if age:
                age = int(age)
            update_voter(voter_id, name, age)
        elif choice == '4':
            voter_id = int(input("Enter voter ID to delete: "))
            delete_voter(voter_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

# Manage Votes submenu
def manage_votes():
    while True:
        print("\nManage Votes:")
        print("1. Cast Vote")
        print("2. View Votes")
        print("3. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            voter_id = int(input("Enter voter ID: "))
            candidate_id = int(input("Enter candidate ID to vote for: "))
            create_vote(voter_id, candidate_id)
        elif choice == '2':
            get_votes()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

# Main function
def main():
    init_db()  # Initialize the database

    welcome()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            manage_candidates()
        elif choice == '2':
            manage_voters()
        elif choice == '3':
            manage_votes()
        elif choice == '4':
            view_results()
        elif choice == '5':
            print("Thanks for using the Online Voting System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
