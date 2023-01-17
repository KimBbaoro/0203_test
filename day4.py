e2f = {"dog" : "chien", "cat" : "chat", "walrus" : "morse"}

ans = [eng for eng, fre in e2f.items() if fre == 'chien']
print(ans[0])
