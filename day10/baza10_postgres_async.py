import asyncio
import asyncpg


#     await conn.fetch("CREATE TABLE IF NOT EXISTS users2 (id SERIAL PRIMARY KEY, name TEXT);")
#     await conn.execute("""
#     INSERT INTO users2 (name) VALUES ($1)
#     """)
#     await conn.close()
#
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(run())
