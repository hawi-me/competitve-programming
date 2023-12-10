class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
    #no lost any machecs mean winnes all
        losses = collections.Counter()
        player=set()
        for winner , losser in matches:
            losses[losser]+=1
            player.add(winner)
            player.add(losser)
        no_lost,one_lost = [] , []
        for players in player:
            if losses[players]== 0:
               no_lost.append(players)
            elif losses[players]==1:
                one_lost.append(players)
        return [sorted(no_lost),sorted(one_lost)]
