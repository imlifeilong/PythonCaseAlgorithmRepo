from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

# 1. 创建引擎（连接 SQLite 数据库，echo=True 会打印执行的 SQL 语句，便于调试）
engine = create_engine("sqlite:///test_orm.db", echo=True)

# 创建 Session 工厂（绑定引擎）
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# 2. 创建 ORM 基类（所有模型类继承此类）
class Base(DeclarativeBase):
    pass


# 模型 1：User（用户表）
class User(Base):
    __tablename__ = "users"  # 数据库表名（必须指定）

    # 字段定义
    id = Column(Integer, primary_key=True, autoincrement=True)  # 自增主键
    name = Column(String(50), nullable=False, index=True)  # 姓名（非空，加索引）
    email = Column(String(100), unique=True, nullable=False)  # 邮箱（唯一，非空）
    age = Column(Integer, default=0)  # 年龄（默认值 0）

    # 关联关系：User -> Post（一对多：一个用户可发表多篇文章）
    posts = relationship("Post", back_populates="author", cascade="all, delete-orphan")

    # 自定义方法：打印对象时的格式
    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, email={self.email})>"


# 模型 2：Post（文章表，与 User 关联）
class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    content = Column(String(500))
    # 外键：关联 User 表的 id 字段
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # 关联关系：Post -> User（多对一：多篇文章属于一个用户）
    author = relationship("User", back_populates="posts")

    def __repr__(self):
        return f"<Post(id={self.id}, title={self.title}, author_id={self.author_id})>"


def create_tables():
    # 创建所有表（若表已存在则跳过）
    Base.metadata.create_all(engine)


# 获取会话实例（每次操作数据库时创建，用完关闭）
def get_db():
    db = SessionLocal()
    try:
        yield db  # 提供会话给业务逻辑
    finally:
        db.close()  # 确保会话关闭，避免连接泄漏


create_tables()

# 1. 新增数据（Create）
db = next(get_db())
# 创建 User 对象
user1 = User(name="Alice", email="alice@example.com", age=28)
# 创建 Post 对象（关联 User）
post1 = Post(title="First Post", content="Hello SQLAlchemy!", author=user1)
# 添加到会话
db.add(user1)
db.add(post1)
# 提交事务（数据写入数据库）
db.commit()
# 刷新对象（获取自增 ID 等数据库生成的字段）
db.refresh(user1)
print(user1)  # 输出：<User(id=1, name=Alice, email=alice@example.com)>

# 2. 查询数据（Read）
# 方式 1：按主键查询
user = db.query(User).get(1)  # 等价于 SELECT * FROM users WHERE id=1
print(user.posts)  # 自动关联查询，输出：[<Post(id=1, title=First Post, author_id=1)>]

# 方式 2：条件查询（过滤、排序、分页）
# 查询年龄 >25 的用户，按姓名排序，取前 10 条
users = db.query(User).filter(User.age > 25).order_by(User.name).limit(10).all()

# 方式 3：关联查询（查询用户及其文章）
user_with_posts = db.query(User).join(Post).filter(Post.title.contains("First")).first()

# 3. 修改数据（Update）
user = db.query(User).get(1)
user.age = 29  # 直接修改对象属性
db.commit()  # 提交事务

# 4. 删除数据（Delete）
post = db.query(Post).get(1)
db.delete(post)  # 从会话中删除对象
db.commit()  # 提交事务（数据库中删除行）

try:
    user2 = User(name="Bob", email="bob@example.com")
    post2 = Post(title="Second Post", author=user2)
    db.add(user2)
    db.add(post2)
    db.commit()  # 执行 db.commit() 时，会话中所有未提交的操作会被打包成一个事务提交到数据库；
except Exception as e:
    db.rollback()  # 执行过程中抛出异常，需调用 db.rollback() 回滚事务，避免数据不一致。
    print(f"Error: {e}")
finally:
    db.close()

from sqlalchemy import text

# 方式 1：用 text() 包装 SQL 字符串（参数化查询，避免 SQL 注入）
result = db.execute(
    text("SELECT name, email FROM users WHERE age > :age"),
    {"age": 25}  # 参数传递
)
for row in result:
    print(row.name, row.email)

# # 方式 2：直接执行 SQL 文件（适合大型 SQL 脚本）
# with open("init_data.sql", "r") as f:
#     sql = f.read()
#     db.execute(text(sql))
#     db.commit()
