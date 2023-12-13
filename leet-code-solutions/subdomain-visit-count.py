class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_count={}
        for domain in cpdomains:
            count,d=domain.split()
            count=int(count)
            d=list(d.split('.'))
            for i in range(len(d)):
                temp = ".".join(d[i:])
                domain_count[temp]=domain_count.get(temp,0)+count
            ans=[]
            for i,j in domain_count.items():
                te=str(j)+" "+i
                ans.append(te)
        return ans