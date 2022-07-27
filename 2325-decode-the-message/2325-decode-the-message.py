class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        k=key.split()
        s=''.join(k)
        l=list(s)
        t=dict.fromkeys(l)
        l4=list(t)
        l1=[]
        ch=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        l2=list(message)
        for i in range(len(l2)):
            for j in range(len(l4)):
                if(l2[i]==l4[j]):
                    l1.append(ch[j])
            if(l2[i]==' '):
                l1.append(l2[i])
        return ''.join(l1)