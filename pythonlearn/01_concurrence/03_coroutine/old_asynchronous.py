import greenlet


class OldAsync:
    gre1 = None
    gre2 = None

    def gre_func1(self):
        print('1111')
        self.gre2.switch()  # 主动切换到方法gre_func2
        print('222')
        self.gre2.switch()

    def gre_func2(self):
        print('333')
        self.gre1.switch()  # 主动切换到方法gre_func1
        print('444')

    def yie_func1(self):
        yield 1
        yield from self.yie_func2()  # 主动切换
        yield 2

    def yie_func2(self):
        yield 3

        yield 4

    def main(self):
        self.gre1 = greenlet.greenlet(self.gre_func1)
        self.gre2 = greenlet.greenlet(self.gre_func2)
        self.gre1.switch()

        print('---------------------')

        for x in self.yie_func1():
            print(x)


if __name__ == '__main__':
    oa = OldAsync()
    oa.main()
