votes = []

def create_vote(voter_id, candidate_id):
    vote = {"voter_id": voter_id, "candidate_id": candidate_id}
    votes.append(vote)
    print(f"Voter {voter_id} voted for Candidate {candidate_id}.")

def get_votes():
    if not votes:
        print("No votes cast yet.")
    else:
        print("\nVotes:")
        for vote in votes:
            print(f"Voter ID: {vote['voter_id']} voted for Candidate ID: {vote['candidate_id']}")

def view_results():
    if not votes:
        print("No votes cast yet.")
        return

    results = {}
    for vote in votes:
        candidate_id = vote['candidate_id']
        results[candidate_id] = results.get(candidate_id, 0) + 1

    print("\nVoting Results:")
    for candidate_id, count in results.items():
        print(f"Candidate ID {candidate_id}: {count} votes")
