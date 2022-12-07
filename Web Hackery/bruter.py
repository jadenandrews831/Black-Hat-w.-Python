import queue
import requests
import threading
import sys

AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15"
EXTENSIONS = ['.php', '.bak', '.orig', '.inc']
TARGET = 'http://testphp.vulnweb.com'
THREADS = 50
WORDLIST = "./all.txt"

def get_words(resume=None):
  def extend_words(word):
    if "." in word:
      words.put(f'/{word}')
    else:
      words.put(f'/{word}/')
    for extension in EXTENSIONS:
      words.put(f'/{word}{extension}')

  with open(WORDLIST) as f:
    raw_words = f.read()
    # print(raw_words)

  found_resume = False
  words = queue.Queue()

  for word in raw_words.split():
    if resume is not None:
      if found_resume:
        extend_words(word)
      elif word == resume:
        found_resume = True
        print(f'Resuming wordlist from: {resume}')
    else:
      print(word)
      extend_words(word)
    
  return words

def dir_bruter(words):
  headers = {'User-Agent': AGENT}
  while not words.empty():
    url = f'{TARGET}{words.get()}'
    try:
      r = requests.get(url, headers=headers)
    except requests.exceptions.ConnectionError:
      sys.stderr.write('x');sys.stderr.flush()
      continue
    
    if r.status_code == 200:
      print(f'\nSuccess ({r.status_code}: {url})')
    elif r.status_code == 404:
      sys.stderr.write('.');sys.stderr.flush()
    else:
      print(f'{r.status_code} => {url}')

if __name__ == '__main__':
  words = get_words()
  print('Press return to continue.')
  sys.stdin.readline()
  for _ in range(THREADS):
    t = threading.Thread(target=dir_bruter, args=(words,))
    t.start()