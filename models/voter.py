voters = []
next_voter_id = 1

def create_voter(name, age):
    global next_voter_id
    voter = {"id": next_voter_id, "name": name, "age": age}
    voters.append(voter)
    next_voter_id += 1
    print(f"Voter {name} added.")

def get_voters():
    if not voters:
        print("No voters available.")
    else:
        print("\nVoters:")
        for voter in voters:
            print(f"ID: {voter['id']}, Name: {voter['name']}, Age: {voter['age']}")

def update_voter(voter_id, name=None, age=None):
    for voter in voters:
        if voter['id'] == voter_id:
            if name:
                voter['name'] = name
            if age:
                voter['age'] = age
            print(f"Voter {voter_id} updated.")
            return
    print(f"Voter {voter_id} not found.")

def delete_voter(voter_id):
    global voters
    voters = [voter for voter in voters if voter['id'] != voter_id]
    print(f"Voter {voter_id} deleted.")
