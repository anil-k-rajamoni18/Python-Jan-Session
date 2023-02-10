def encrpyData(data):
  for dt in data:

    for k , v in dt.items():
      if k=="passwd":
        dt["passwd"] = encrpyPassword(v)
  return data

def encrpyPassword(passwd):
  import hashlib

  return hashlib.md5(passwd.encode()).hexdigest()