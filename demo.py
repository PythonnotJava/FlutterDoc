import weakref


class Publisher:
    """新闻发布者类，管理订阅者并发布新闻"""

    def __init__(self):
        self._subscribers = set()  # 订阅者集合

    def subscribe(self, subscriber):
        """订阅新闻"""
        self._subscribers.add(weakref.ref(subscriber))  # 使用 weakref 以避免强引用

    def unsubscribe(self, subscriber):
        """取消订阅"""
        self._subscribers = {sub for sub in self._subscribers if sub() != subscriber}

    def publish(self, news):
        """发布新闻，通知所有订阅者"""
        for subscriber_ref in list(self._subscribers):
            subscriber = subscriber_ref()  # 获取订阅者对象
            if subscriber:
                subscriber.update(news)  # 通知订阅者


class Subscriber:
    """订阅者类，响应新闻发布"""

    def __init__(self, name):
        self.name = name

    def update(self, news):
        """处理新闻的更新"""
        print(f"{self.name} received news: {news}")


# 使用示例
if __name__ == "__main__":
    # 创建发布者
    publisher = Publisher()

    # 创建订阅者
    subscriber1 = Subscriber("Alice")
    subscriber2 = Subscriber("Bob")

    # 订阅新闻
    publisher.subscribe(subscriber1)
    publisher.subscribe(subscriber2)

    # 发布新闻
    publisher.publish("Breaking News: Python 3.12 Released!")

    # 取消 Bob 的订阅
    publisher.unsubscribe(subscriber2)

    # 发布新的新闻
    publisher.publish("New Development in Python AI Library!")
