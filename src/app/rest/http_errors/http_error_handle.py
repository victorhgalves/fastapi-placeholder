from fastapi import HTTPException
from src.app.exceptions.business_exception import BusinessException


from enum import Enum
class CustomErrors(Enum):
    without_authorization_header = "without_authorization_header"


dict_errors = {
                CustomErrors.without_authorization_header.value:HTTPException(status_code=403, detail="Request without Authorization Header"),
            }
