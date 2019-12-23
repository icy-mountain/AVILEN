if __name__ == "__main__":
  with open("input.txt","r") as f:
    a = f.read()
    list_ = a.split("\n")
    # print(list_)
    num = int(list_[-2])
  # print(num)
  dic = {}
  for i in list_[:-2]:
    hoge = i.split(":")
    dic[hoge[1]] = int(hoge[0])
  # print(dic)
  sorted = sorted(dic.items(), key=lambda x:x[1])
  ans = ""
  for i in sorted:
    if num%i[1] == 0:
      ans += i[0]
  if ans == "":
    ans = num
  print(ans)






  

