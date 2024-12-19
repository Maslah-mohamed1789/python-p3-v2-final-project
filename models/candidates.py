candidates = []
next_candidate_id = 1

def create_candidate(name, party):
    global next_candidate_id
    candidate = {"id": next_candidate_id, "name": name, "party": party}
    candidates.append(candidate)
    next_candidate_id += 1
    print(f"Candidate {name} from {party} added.")

def get_candidates():
    if not candidates:
        print("No candidates available.")
    else:
        print("\nCandidates:")
        for candidate in candidates:
            print(f"ID: {candidate['id']}, Name: {candidate['name']}, Party: {candidate['party']}")

def update_candidate(candidate_id, name=None, party=None):
    for candidate in candidates:
        if candidate['id'] == candidate_id:
            if name:
                candidate['name'] = name
            if party:
                candidate['party'] = party
            print(f"Candidate {candidate_id} updated.")
            return
    print(f"Candidate {candidate_id} not found.")

def delete_candidate(candidate_id):
    global candidates
    candidates = [candidate for candidate in candidates if candidate['id'] != candidate_id]
    print(f"Candidate {candidate_id} deleted.")
