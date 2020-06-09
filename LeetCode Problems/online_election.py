from bisect import bisect_right
class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        self.candidates, top_candidate = {persons[0]: 1}, persons[0]
        self.top_candidate_at_time, self.times = {times[0]: persons[0]}, times
        for i in range(1, len(persons)):
            person, time = persons[i], times[i]
            if person not in self.candidates:
                self.candidates[person] = 0
            self.candidates[person] += 1
            if self.candidates[person] >= self.candidates[top_candidate]:
                top_candidate = person
            self.top_candidate_at_time[time] = top_candidate
        
    def q(self, t: int) -> int:
        return self.top_candidate_at_time[self.times[bisect_right(self.times, t) - 1]]
