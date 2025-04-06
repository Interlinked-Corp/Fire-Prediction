import os
from constants import DEBUG_LOG

def getPathFromEnv(defaultPrefix = os.getenv('DEFAULT_PREFIX', '')):
  def usePrefix(envKey: str, *paths: str):
    return os.path.join(defaultPrefix, os.getenv(envKey, ''), *paths)
  return usePrefix

if DEBUG_LOG:
  print(os.getenv('DEFAULT_PREFIX'))