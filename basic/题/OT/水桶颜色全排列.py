class Solution:
    def permute(self):
        self.mapping = [
            ['红盖', '黄盖', '蓝盖', '绿盖', '紫盖', '白盖'],
            ['红桶', '黄桶', '蓝桶', '绿桶', '紫桶', '白桶'],
        ]
        self.result = []
        self.backtrack(0, [])
        return self.result

    def backtrack(self, index, tmp):
        # index 递归的深度
        # tmp 临时栈，用于记录符合条件的元素

        # 递归的深度达到2时，终止递归，因为只有2种元素进行全排列
        if index == 2:
            # 止痛剂桶盖和桶身颜色不同的情况
            if tmp[0][0] != tmp[1][0]:
                self.result.append(tmp[:])
            return

        datalist = self.mapping[index]
        for i in range(len(datalist)):
            tmp.append(datalist[i])
            # 将元素入栈后，去下一层进行试探
            self.backtrack(index + 1, tmp)
            tmp.pop()


if __name__ == '__main__':
    s = Solution()
    res = s.permute()
    print(len(res), res)
