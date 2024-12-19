from database.db_setup import execute_query, fetch_all, fetch_one

def create_candidate(name, party):
    """Adds a new candidate to the database."""
    query = 'INSERT INTO candidates (name, party) VALUES (?, ?)'
    execute_query(query, (name, party))
    print(f"Candidate {name} from {party} added.")

def get_candidates():
    """Fetches and displays all candidates."""
    query = 'SELECT * FROM candidates'
    candidates = fetch_all(query)
    if not candidates:
        print("No candidates available.")
    else:
        print("\nCandidates:")
        for candidate in candidates:
            print(f"ID: {candidate[0]}, Name: {candidate[1]}, Party: {candidate[2]}")

def update_candidate(candidate_id, name=None, party=None):
    """Updates a candidate's details in the database."""
    query = 'UPDATE candidates SET name = ?, party = ? WHERE id = ?'
    execute_query(query, (name or '', party or '', candidate_id))
    print(f"Candidate {candidate_id} updated.")

def delete_candidate(candidate_id):
    """Deletes a candidate from the database."""
    query = 'DELETE FROM candidates WHERE id = ?'
    execute_query(query, (candidate_id,))
    print(f"Candidate {candidate_id} deleted.")
