"""
备忘录模式是一种行为型设计模式，它允许在不暴露对象实现细节的情况下保存和恢复对象的状态。备忘录模式主要包含三个角色：发起人（Originator）、备忘录（Memento）、负责人（Caretaker）。

发起人（Originator）：负责创建一个包含自身状态的备忘录对象，并可以使用备忘录对象恢复其状态。

备忘录（Memento）：负责存储发起人的状态，以便在需要时可以恢复到先前的状态。

负责人（Caretaker）：负责保存备忘录对象，但并不了解备忘录的具体内容。负责人可以存储和检索备忘录，但不应该修改备忘录的内容。

优点：
封装性好：备忘录模式将对象状态的保存和恢复封装在备忘录中，提高了对象的封装性。

维护性好：备忘录模式将备忘录对象的责任分离到不同的类中，易于维护和修改。

支持撤销和恢复功能：备忘录模式可以支持对象的撤销和恢复功能，使得对象的状态可以在不同时间点进行切换。

缺点：
资源消耗较大：如果备忘录对象包含的状态信息过多，可能会导致资源消耗较大。

可能引起性能问题：频繁保存和恢复状态可能会引起性能问题，尤其是在状态信息较大的情况下。

实际开发中的使用：
备忘录模式在实际开发中常用于以下场景：

需要保存和恢复对象状态的场景：当需要保存对象的状态，以便在需要时恢复到先前状态时，可以考虑使用备忘录模式。

支持撤销和恢复功能的场景：当需要实现撤销和恢复功能时，备忘录模式是一种常见的实现方式。
"""


# 备忘录类
class EditorMemento:
    def __init__(self, content):
        self._content = content

    def get_content(self):
        return self._content


# 发起人类
class TextEditor:
    def __init__(self):
        self._content = ""

    def write(self, text):
        self._content += text

    def save(self):
        return EditorMemento(self._content)

    def restore(self, memento):
        self._content = memento.get_content()

    def show_content(self):
        print(f"Current Content: {self._content}")


# 负责人类
class History:
    def __init__(self):
        self._history = []

    def add_memento(self, memento):
        self._history.append(memento)

    def get_memento(self, index):
        return self._history[index]


# 客户端代码
if __name__ == "__main__":
    # 创建文本编辑器
    editor = TextEditor()
    history = History()

    # 编辑文本
    editor.write("Hello, ")
    editor.show_content()  # 输出 "Current Content: Hello, "

    # 保存备忘录
    memento1 = editor.save()
    history.add_memento(memento1)

    # 继续编辑文本
    editor.write("World!")
    editor.show_content()  # 输出 "Current Content: Hello, World!"

    # 保存备忘录
    memento2 = editor.save()
    history.add_memento(memento2)

    # 恢复到先前状态
    editor.restore(history.get_memento(0))
    editor.show_content()  # 输出 "Current Content: Hello, "
