import asyncio
import random

#ANSI colors
c =(
    "\033[0m",
    "\033[36m", #cyan
    "\033[91m",#czerwień
    "\033[35m" #magenta
)


async def makerandom(idx:int,threshold:int=6)->int:
    print(f"{c[idx+1]} inicjacja makerandom({idx}).")
    i = random.randint(0,10)
    while i <= threshold:
        print(f"{c[idx+1]} makerandom({idx})=={i} zbyt niska wartość, powtórzenie...")
        await asyncio.sleep(idx+1)
        i = random.randint(0,10)
    print(f"{c[idx + 1]} zakończono: makerandom({idx}) == {i} {c[0]}.")
    return i

async def main():
    res = await asyncio.gather(*(makerandom(i,9-i) for i in range(3)))
    return res

if __name__ == '__main__':
    random.seed(444)
    r1,r2,r3 = asyncio.run(main())
    print()
    print(f"wyniki -> r1: {r1}, r2: {r2}, r3: {r3}")



