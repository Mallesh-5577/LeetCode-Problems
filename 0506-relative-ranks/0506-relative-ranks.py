class Solution(object):
    def findRelativeRanks(self, score):
        rank_index = list(range(len(score)))
        for i in range(len(score)):
            score_index = i
            for j in range(i+1,len(score)):
                if score[j]>score[score_index]:
                    score_index = j
            score[i],score[score_index]=score[score_index],score[i]
            rank_index[i],rank_index[score_index]=rank_index[score_index],rank_index[i]
        
        res = [0]*len(score)

        for rank in range(len(score)):
            if rank==0:
                res[rank_index[rank]]="Gold Medal"
            elif rank==1:
                res[rank_index[rank]]="Silver Medal"
            elif rank==2:
                res[rank_index[rank]]="Bronze Medal"
            else:
                res[rank_index[rank]]=str(rank+1)
        return res
            