from modules import hello     # file ko jub module ke under hai to uska naam dekar import + filename dekar use karsakte hai
import modules                # if  __init__.py file ke under hai function to directly import karke use karsakte hai

test = modules.test()
print(hello)   