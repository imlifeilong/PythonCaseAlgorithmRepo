"""
享元模式是一种结构型设计模式，它旨在减少对象的数量，以节省内存和提高性能。在享元模式中，共享的对象被多个相似对象共用，从而减少了对内存的占用。

享元模式适用于存在大量相似对象的情况，其中相似对象的大部分状态是相同的，而只有一小部分状态需要单独存储。享元模式将这些相同的状态提取出来，形成共享的对象，其他对象只需存储自己的特有状态。

优点：
减少内存占用：通过共享相同状态的对象，减少了内存的使用，提高了系统的性能。

提高性能：减少了创建和销毁对象的开销，提高了系统的性能。

简化代码：享元模式将对象的共享状态抽取出来，使得系统中的对象更简单，易于维护。

缺点：
不适用于所有情况：享元模式适用于大量相似对象的情况，如果对象之间差异较大，可能无法受益于享元模式。

增加了复杂性：引入共享对象池和对共享状态的管理可能会增加系统的复杂性。

实际开发中的使用：
在实际开发中，享元模式常常用于以下场景：

文本编辑器中的字符共享：在文本编辑器中，字符可以看作是享元对象，相同的字符在内存中只存储一份，不同的文本区域共享相同的字符。

游戏开发中的对象池：在游戏中，如果存在大量相似的对象，可以使用享元模式将这些相似对象池化，减少内存占用和提高性能。
"""


# 享元工厂类
class CharacterFactory:
    def __init__(self):
        self._characters = {}

    def get_character(self, char):
        if char not in self._characters:
            self._characters[char] = Character(char)
        return self._characters[char]


# 享元类
class Character:
    def __init__(self, char):
        self.char = char

    def display(self, font_size):
        return f"字母 '{self.char}' 大小设置为 {font_size}"


# 客户端代码
if __name__ == "__main__":
    # 创建享元工厂
    factory = CharacterFactory()

    # 获取并显示共享的字符对象
    char1 = factory.get_character('A')
    char2 = factory.get_character('A')
    char3 = factory.get_character('B')

    # 通过id查看字符对象是否是同一个
    print(id(char1), char1.display(12))  # 输出 "Character 'A' with font size 12"
    print(id(char2), char2.display(16))  # 输出 "Character 'A' with font size 16"
    print(id(char3), char3.display(14))  # 输出 "Character 'B' with font size 14"
