"""
策略模式是一种行为型设计模式，它定义了一系列算法，将每个算法封装起来，并且使它们可以互换。策略模式允许客户端在运行时选择算法的实现，而不是在编译时固定使用某个算法。

在策略模式中，算法被定义成独立的策略类，客户端通过使用不同的策略对象来选择不同的算法。这种方式使得算法可以独立于客户端而变化，客户端不需要知道具体算法的实现细节。

优点：
灵活性：策略模式允许客户端在运行时选择算法，提供了更灵活的算法切换方式。

复用性：策略模式将算法封装成独立的策略类，使得算法可以被复用，降低了代码的重复性。

易于扩展：新增算法只需要增加新的策略类，不需要修改原有代码，易于扩展。

缺点：
客户端需要了解所有的策略类：客户端在选择算法时需要了解所有可用的策略类，可能会增加客户端的复杂性。

增加了对象数量：每个算法都会对应一个策略类，可能会增加对象的数量。

实际开发中的使用：
策略模式在实际开发中常用于以下场景：

算法的选择需要在运行时确定：如果算法的选择需要在运行时确定，并且需要灵活切换，策略模式是一个合适的选择。

避免使用条件语句选择算法：当有多个条件语句用于选择不同的算法时，可以考虑使用策略模式来避免条件语句的过度复杂。
"""


# 策略接口
class PaymentStrategy:
    def pay(self, amount):
        pass


# 具体策略A
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        return f"刷信用卡支付 {amount} "


# 具体策略B
class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        return f"PayPal在线支付 {amount} "


# 具体策略C
class BankTransferPayment(PaymentStrategy):
    def pay(self, amount):
        return f"银行卡支付 {amount} "


# 上下文类
class ShoppingCart:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def checkout(self, amount):
        return self.payment_strategy.pay(amount)


# 客户端代码
if __name__ == "__main__":
    # 创建不同的支付策略
    credit_card_payment = CreditCardPayment()
    paypal_payment = PayPalPayment()
    bank_transfer_payment = BankTransferPayment()

    # 创建购物车，并选择支付策略
    cart1 = ShoppingCart(credit_card_payment)
    cart2 = ShoppingCart(paypal_payment)
    cart3 = ShoppingCart(bank_transfer_payment)

    # 结账
    print(cart1.checkout(100))  # 输出 "Paying 100 via Credit Card"
    print(cart2.checkout(150))  # 输出 "Paying 150 via PayPal"
    print(cart3.checkout(200))  # 输出 "Paying 200 via Bank Transfer"
