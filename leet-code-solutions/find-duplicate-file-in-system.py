class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        file_dictionary= defaultdict(list)
        for i in range(len(paths)):
            p=paths[i].split()
            dirctory=p[0]
            for d in range(1,len(p)):
                file_name,content=p[d].split('(')
                file_dictionary[content].append(f"{dirctory}/{file_name}")
        print(file_dictionary)
        output=[]
        for val in file_dictionary.values():
            if len(val) > 1:
               output.append(val)
        return output
            




