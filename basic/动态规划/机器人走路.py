class RobotWalk(object):
    def ways_a(self, pos, steps, start, target):
        """

        :param pos: 总共有pos个位置
        :param steps: 可以走的步数
        :param start: 开始位置
        :param target: 目标位置
        :return:
        """
        if pos < 2 or steps < 1 or start < 1 or start > pos or target < 1 or target > pos:
            return 0
        return self.process_a(pos, start, steps, target)

    def process_a(self, pos, cur, rest, target):
        """
        :param pos: 总共有pos个位置
        :param cur: 当前来到的位置
        :param rest: 还剩下的步数
        :param target: 目标位置
        :return: 机器人从cur出发，走过rest步之后，最终停留在target的方法数
        """
        # 步数走完时，如果机器人刚好到达目标位置，则返回1
        if rest == 0:
            return 1 if cur == target else 0
        # 如果在1位置，只能向右走 -> cur+1
        if cur == 1:
            return self.process_a(pos, cur + 1, rest - 1, target)
        # 如果在最后一个位置，只能向左 -> cur-1
        if cur == pos:
            return self.process_a(pos, cur - 1, rest - 1, target)
        # 中间位置 既能向左又能向右
        return self.process_a(pos, cur + 1, rest - 1, target) + self.process_a(pos, cur - 1, rest - 1, target)

    def ways_b(self, pos, steps, start, target):
        """

        :param pos: 总共有pos个位置
        :param steps: 可以走的步数
        :param start: 开始位置
        :param target: 目标位置
        :return:
        """
        if pos < 2 or steps < 1 or start < 1 or start > pos or target < 1 or target > pos:
            return 0
        # 转移条件 剩下的步数 和 当前位置
        # 当前位置cur 范围 1~pos
        # 剩余步数rest 范围 0~steps
        # steps（总步数） 列 pos（总共位置数） 行的数组
        cache = [[-1] * (steps + 1) for _ in range(pos + 1)]
        return self.process_b(pos, start, steps, target, cache)

    def process_b(self, pos, cur, rest, target, cache):
        """
        加缓存减少重复计算
        :param pos:
        :param cur:
        :param rest:
        :param target:
        :param cache:
        :return:
        """
        # 当前位置没有计算过，则计算后存入缓存，否则直接返回缓存数据
        if cache[cur][rest] == -1:
            # 步数走完时，如果机器人刚好到达目标位置，则返回1
            if rest == 0:
                index = 1 if cur == target else 0
            elif cur == 1:
                index = self.process_b(pos, 2, rest - 1, target, cache)
            elif cur == pos:
                index = self.process_b(pos, pos - 1, rest - 1, target, cache)
            else:
                index = self.process_b(pos, cur + 1, rest - 1, target, cache) + \
                        self.process_b(pos, cur - 1, rest - 1, target, cache)
            cache[cur][rest] = index
        return cache[cur][rest]

    def ways_c(self, pos, steps, start, target):
        """
        :param pos: 总共有pos个位置
        :param steps: 可以走的步数
        :param start: 开始位置
        :param target: 目标位置
        :return:
        """
        if pos < 2 or steps < 1 or start < 1 or start > pos or target < 1 or target > pos:
            return 0
        # 当前位置cur 范围 1~pos
        # 剩余步数rest 范围 0~steps
        # steps（总步数） 列 pos（总共位置数） 行的数组
        dp = [[0] * (steps + 1) for _ in range(pos + 1)]
        # 当剩余0步时，刚好来到target位置 则dp值为1， 其他位置值为0
        dp[target][0] = 1
        # 列
        for col in range(1, steps + 1):
            # 第一行依赖左下元素
            dp[1][col] = dp[2][col - 1]
            # 中间行依赖左下和左上
            for row in range(1, pos):
                dp[row][col] = dp[row + 1][col - 1] + dp[row - 1][col - 1]
            # 最末行依赖左上元素
            dp[pos][col] = dp[pos - 1][col - 1]
        for r in dp:
            print(r)
        print(start, steps)
        return dp[start][steps]


if __name__ == '__main__':
    rw = RobotWalk()
    # [ 位置数, 剩余步数, 当前位置, 目标位置]
    x = [6, 5, 1, 4]
    a = rw.ways_a(*x)
    print(a)
    b = rw.ways_b(*x)
    print(b)
    c = rw.ways_c(*x)
    print(c)
