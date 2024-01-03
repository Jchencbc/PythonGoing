"""
协程：python3.4之后引入asyncio
"""
import asyncio

async def func_io():
    print('工作已开始')
    await asyncio.sleep(2)  # io等待时await关键词切换任务
    print('工作已结束')

async def main():
    print('主流程')
    
    task_list = [
        asyncio.create_task(func_io(), name='t1'),
        asyncio.create_task(func_io(), name='t2'),
    ]  # 创建io任务
    
    done, pending = await asyncio.wait(task_list, timeout=None)  # asyncio.wait等待任务列表启动
    print(done)

asyncio.run(main())