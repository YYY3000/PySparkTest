import redis

r = redis.Redis("127.0.0.1", 6379, 0, "123456")
r.set("yyy_test_1", "1")
r.set("yyy_test_2", "2")
r.set("yyy_test_3", "3")
ls = r.keys("yyy_test_*")
for i in range(len(ls)):
    print(ls[i])
    r.delete(ls[i])
