### Config details
import os

### Database
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "")
DB_PW = os.getenv("DB_PW", "")
DB_INDEX = os.getenv("DB_INDEX", "document")


### Reader
READER_MODEL_PATH = os.getenv("READER_MODEL_PATH", "deepset/roberta-base-squad2-covid")
CONTEXT_WINDOW_SIZE = int(os.getenv("CONTEXT_WINDOW_SIZE", 500))
DEFAULT_TOP_K_READER = int(os.getenv("DEFAULT_TOP_K_READER", 5))
TOP_K_PER_CANDIDATE = int(os.getenv("TOP_K_PER_CANDIDATE", 3))
NO_ANS_BOOST = int(os.getenv("NO_ANS_BOOST", -10))
DOC_STRIDE = int(os.getenv("DOC_STRIDE", 128))
MAX_SEQ_LEN = int(os.getenv("MAX_SEQ_LEN", 256))



### Retriever


