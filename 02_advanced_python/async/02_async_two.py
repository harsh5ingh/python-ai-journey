import asyncio
import time

async def brew(name):
  print(f"Brewing {name}...")
  await asyncio.sleep(2)
  # time.sleep(3)
  print(f"{name} is ready....")


async def main():
  await asyncio.gather(
    brew("Masala chai"),
    brew("Green Chai"),
    brew("Ginger Chai"),
  )

asyncio.run(main())