from src.utils.os_utils import getPathFromEnv
from constants import DEBUG_LOG

FIRE_STATISTICS_CSV = getPathFromEnv()('FIRE_STATISTICS_CSV')

if DEBUG_LOG:
    print(FIRE_STATISTICS_CSV)
    print("Config loaded successfully")
