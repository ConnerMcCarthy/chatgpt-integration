import os.path

import openai
import gkeepapi

noteID = '1bX2GAEjz0u-Ea7FIsQ0CdvVtdy5AeOjaSJ5P9ZRq9oY1S3p1cSYY_k5fn-5VVw'

def main():
    keep = gkeepapi.Keep()
    keep.login('mcconner97@gmail.com', 'password')
    
    gnote = keep.get(noteID)
    print(gnote.title)
    print(gnote.text)

if __name__ == '__main__':
    main()