"""
组合模式是一种结构型设计模式，它将对象组合成树形结构以表示“部分-整体”的层次结构。组合模式允许客户端使用单个对象和组合对象（对象的集合）一样对待，从而使得客户端无需关心它们之间的差异。

组合模式有两种主要类型的对象：

叶子（Leaf）：是组合中的叶子节点，它没有子节点。
组合（Composite）：是具有子节点的复合节点，它可以包含叶子节点和其他组合节点。
优点：
统一接口：组合模式使得客户端可以统一地使用单个对象和组合对象，因为它们都实现了相同的接口。

灵活性：可以通过组合不同的叶子和组合对象来构建复杂的树形结构，从而实现灵活的对象组合。

易扩展：添加新的叶子或组合节点非常容易，无需修改现有代码。

缺点：
可能过于一般化：有时候，组合模式可能过于一般化，导致在处理一些特定需求时可能变得复杂。

可能难以限制组合中的成分：组合模式中的组合对象可以包含任意数量的叶子和其他组合对象，这可能导致难以限制组合中的成分。

实际开发中的使用：
组合模式在实际开发中常用于处理树形结构的问题，例如图形界面中的控件布局、文件系统的目录结构等
"""


# 组合抽象类
class Component:
    def __init__(self, name):
        self.name = name

    def display(self):
        pass


# 叶子类 - 文件
class File(Component):
    def display(self):
        print(f"文件: {self.name}")


# 组合类 - 目录
class Directory(Component):
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def display(self):
        print(f"目录: {self.name}")
        for child in self.children:
            child.display()


# 客户端代码
if __name__ == "__main__":
    # 创建文件和目录对象
    file1 = File("file1.txt")
    file2 = File("file2.txt")

    directory1 = Directory("文件夹 1")
    directory1.add(file1)

    directory2 = Directory("文件夹 2")
    directory2.add(file2)

    root_directory = Directory("根目录")
    root_directory.add(directory1)
    root_directory.add(directory2)

    # 显示整个文件系统结构
    root_directory.display()
