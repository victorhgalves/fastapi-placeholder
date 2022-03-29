from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class BaseSchema(BaseModel):
    status_code: int
    server_unix_timestamp : int
    response_data: Optional[dict]

class BaseSuccessSchema(BaseSchema):
    def __init__(self, *args, **kwargs):
        status_code = 100
        server_unix_timestamp = datetime.now().timestamp()
        super().__init__(status_code= status_code, server_unix_timestamp=server_unix_timestamp, response_data=kwargs)
