class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains=defaultdict(int)
        result=[]

        for j in range(len(cpdomains)):

            splitted=cpdomains[j].split()
            parts = splitted[1].split('.')
    
            for i in range(len(parts)):
                parts[i]='.'.join(parts[i:])
            for k in parts:
                domains[k]+=int(splitted[0])
    
        for i in domains:
            result.append(str(domains[i])+ " " + i)
            
        return result