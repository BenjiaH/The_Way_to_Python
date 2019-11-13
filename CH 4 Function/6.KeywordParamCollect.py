def test(num, *books, **scores):
    print("num:", num)
    print("books:", books)
    print("scores:", scores)


test(5, "fkjava", "crazyit", "wawa", 语文=90, 数学=92)
