# 异步连接 URL 格式
# "sqlite+aiosqlite:///相对路径/数据库名.db"
# "sqlite+aiosqlite:////绝对路径/数据库名.db" (Windows 上是 "sqlite+aiosqlite:///C:/path/to/db.db")

# 示例：连接一个名为 async_test.db 的文件数据库
from sqlalchemy.ext.asyncio import create_async_engine

DATABASE_URL = "sqlite+aiosqlite:///./async_test.db"
engine = create_async_engine(DATABASE_URL, echo=True)  # echo=True 会打印 SQL，便于调试

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

# 创建一个异步的 SessionLocal 工厂
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,  # 关键：指定会话类为 AsyncSession
    expire_on_commit=False,  # 建议设置为 False，避免在 commit 后自动过期对象
    autocommit=False,
    autoflush=False,
)

import asyncio
from sqlalchemy import Column, Integer, String, select
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

# --- 1. 初始化 ---

# 数据库连接 URL
DATABASE_URL = "sqlite+aiosqlite:///./async_test.db"

# 创建异步引擎
engine = create_async_engine(DATABASE_URL, echo=True, connect_args={"check_same_thread": False})

# 创建异步会话工厂
AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

# 声明基类
Base = declarative_base()


# --- 2. 定义数据模型 ---

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}')>"


# --- 3. 数据库操作函数 ---

# 初始化数据库（创建表）
async def init_db():
    async with engine.begin() as conn:
        # 在异步模式下，使用 run_sync 来执行同步的 MetaData.create_all
        await conn.run_sync(Base.metadata.create_all)


# 获取数据库会话
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()


# 创建新用户
async def create_user(db: AsyncSession, name: str, email: str):
    db_user = User(name=name, email=email)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


# 获取用户
async def get_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).filter(User.id == user_id))
    return result.scalar_one_or_none()


# --- 4. 主函数 ---

async def main():
    # 1. 初始化数据库，创建表
    await init_db()
    print("数据库和表已创建。")

    # 2. 创建一个新用户
    async with AsyncSessionLocal() as db:
        new_user = await create_user(db, name="异步测试用户", email="async@example.com")
        print("创建的新用户:", new_user)

    # 3. 查询刚刚创建的用户
    async with AsyncSessionLocal() as db:
        fetched_user = await get_user(db, user_id=new_user.id)
        print("查询到的用户:", fetched_user)


if __name__ == "__main__":
    asyncio.run(main())
