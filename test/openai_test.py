from langcache.adapter.openai import OpenAI
from langcache.core import Cache

cache = Cache(tune_frequency=0, tune_policy="recall")
client = OpenAI(cache)

# cache.put("a")

for i in range(2):
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
      {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
  )
  print(completion)
