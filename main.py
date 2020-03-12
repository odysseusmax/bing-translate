import httpx


endpoint = "https://www.bing.com/ttranslatev3"
headers = {
  'origin': 'https://www.bing.com',
  'referer': 'https://www.bing.com/translator/',
  'user-agent' : "Mozilla/5.0 (X11; Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"
}
        
def translate(self, text, to, fromLang='auto-detect'):
  data = {
    'fromLang': fromLang,
    'text': text,
    'to': to
  }
  r = httpx.post(
    endpoint,
    headers = headers,
    data = data
  )
  json = r.json()
  return json

if __name__ == "__main__":
  text = "bonjour comment puis-je vous aider"
  to = 'en'
  translated = translate(text, to)
  print(translate)
