import os
from dotenv import load_dotenv
# utils: 
load_dotenv()  # 加载.env文件
def str_to_bool(value):
    """convert string to bool"""
    true_values = {'true', 'yes', '1', 'on', 't', 'y'}
    false_values = {'false', 'no', '0', 'off', 'f', 'n'}
    
    if isinstance(value, bool):
        return value
        
    if not value:
        return False
        
    value = str(value).lower().strip()
    if value in true_values:
        return True
    if value in false_values:
        return False
    return True  # default return True


DOCKER_WORKPLACE_NAME = os.getenv('DOCKER_WORKPLACE_NAME', 'workplace_meta')
GITHUB_AI_TOKEN = os.getenv('GITHUB_AI_TOKEN', None)
AI_USER = os.getenv('AI_USER', None)
LOCAL_ROOT = os.getenv('LOCAL_ROOT', os.getcwd())

DEBUG = str_to_bool(os.getenv('DEBUG', True))

DEFAULT_LOG = str_to_bool(os.getenv('DEFAULT_LOG', False))
LOG_PATH = os.getenv('LOG_PATH', None)
EVAL_MODE = str_to_bool(os.getenv('EVAL_MODE', False))
BASE_IMAGES = os.getenv('BASE_IMAGES', "tjbtech1/gaia-bookworm:v2-amd64")

COMPLETION_MODEL = os.getenv('COMPLETION_MODEL', "claude-3-5-haiku-20241022")
EMBEDDING_MODEL = os.getenv('EMBEDDING_MODEL', "text-embedding-3-small")

MC_MODE = str_to_bool(os.getenv('MC_MODE', False))

# add Env for function call and non-function call

FN_CALL = str_to_bool(os.getenv('FN_CALL', True))
API_BASE_URL = os.getenv('API_BASE_URL', None)
ADD_USER = str_to_bool(os.getenv('ADD_USER', False))

NON_FN_CALL = str_to_bool(os.getenv('NON_FN_CALL', False))

NOT_SUPPORT_SENDER = ["mistral", "groq"]

if EVAL_MODE:
    DEFAULT_LOG = False

