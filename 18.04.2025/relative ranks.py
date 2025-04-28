Class Solution(object):

    Def findRelativeRanks(self, score):

        Sorted_scores = sorted(score, reverse=True)

        Ranks = {sorted_scores[i]: str(i + 1) for i in range(len(score))}

        Ranks[sorted_scores[0]] = “Gold Medal”

        If len(score) > 1:

            Ranks[sorted_scores[1]] = “Silver Medal”

        If len(score) > 2:

            Ranks[sorted_scores[2]] = “Bronze Medal”

        Return [ranks[s] for s in score]

