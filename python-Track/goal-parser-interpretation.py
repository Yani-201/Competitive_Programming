class Solution:
    def interpret(self, command: str) -> str:
        parsed = ""
        i=0
        while i<len(command):
            if command[i] =="G":
                parsed+="G"
                i+=1

            elif command[i] =="(" and command[i+1] == ")":
                parsed+="o" 
                i+=2

            elif command[i]=="(" and command[i+1] =="a" : 
                parsed+="al"
                i+=4
                
        return parsed
