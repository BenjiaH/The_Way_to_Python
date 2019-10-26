s = "fkjava.org"
# 根据下标访问
print(s[3])
# 指定开始、结束
print(s[2: 4])
# 指定开始、结束、步长
print(s[2: 6: 2])

print("org" in s)
print("ork" in s)
print(len(s))
print(max(s))
print(min(s))

# 字符串的方法
print(s.upper())
print(s.title())

# dir 可以查看某个类的所有方法
print(s.islower())

s1 = " fkjava "
print(s1)
print(s1.lstrip())
print(s1.rstrip())
print(s1.strip())

s2 = "fkjava.org"

s3 = "fkjava.org.wav"
print(s3.split("."))
print("=".join(s3.split(".")))

angle = 5
str1 = "insert into "
str2 = "angel" + str(angle)
str3 = "(index, ch1, ch2, ch3, ch4) "
str4 = "values('%d','%d','%d','%d')"
sql = str1 + str2 + str3 + str4
print(sql)
