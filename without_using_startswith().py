#word and prefix
word = "unwarp"
prefix = "un"
#check if with prefix
if word[:len(prefix)] == prefix:
    print("With prefix")
else:
    print("Without prefix")
