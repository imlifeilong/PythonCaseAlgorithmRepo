'''
# 有1 5 10 20 100 200面额的钞票无穷多，现在使用这些钞票支付X元，最少需要多少？
# 列如，X = 628
# 最佳的支付方法： 3张200，1张20，1张5，3张1

问题：
	1、不能保证最后的解是最优的，如果硬币单位是[1, 4, 6]，兑换8的话，最少的应该是2个4，
	但是使用该算法，得到的结果是1个6，2个1
	2、不能用来求最值问题

'''



def change_coin(much):
	# 币面额
	coins = [200, 100, 20, 10, 5, 1]
	demo = {}

	for x in coins:
		used = much // x  # 需要该面额的多少张
		
		if used > 0:
			demo[x] = used

		much = much % x   # 得到剩余的面额

	return demo, sum(demo.values())

if __name__ == '__main__':
	demo, count = change_coin(628)
	print(demo, count)