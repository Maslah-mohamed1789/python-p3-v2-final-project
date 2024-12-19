from database.db_setup import execute_query
from database.db_setup import fetch_all

def create_vote(voter_id, candidate_id):
    """Records a vote for a given voter and candidate."""
    query = 'INSERT INTO votes (voter_id, candidate_id) VALUES (?, ?)'
    execute_query(query, (voter_id, candidate_id))
    print(f"Vote recorded for Voter {voter_id} on Candidate {candidate_id}.")

def get_votes():
    """Fetches all votes from the database."""
    query = 'SELECT * FROM votes'
    return fetch_all(query)

def view_results():
    """Displays the vote results by candidate."""
    query = '''
    SELECT candidates.name, COUNT(votes.id) AS vote_count
    FROM votes
    JOIN candidates ON votes.candidate_id = candidates.id
    GROUP BY votes.candidate_id
    ORDER BY vote_count DESC
    '''
    results = fetch_all(query)
    for result in results:
        print(f"{result[0]}: {result[1]} votes")
