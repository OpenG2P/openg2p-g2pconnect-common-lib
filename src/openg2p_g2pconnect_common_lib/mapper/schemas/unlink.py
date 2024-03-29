from enum import Enum
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

from ...common.schemas import StatusEnum


class UnlinkStatusReasonCode(Enum):
    rjct_reference_id_invalid = "rjct.reference_id.invalid"
    rjct_reference_id_duplicate = "rjct.reference_id.duplicate"
    rjct_timestamp_invalid = "rjct.timestamp.invalid"
    rjct_beneficiary_name_invalid = "rjct.beneficiary_name.invalid"


class SingleUnlinkRequest(BaseModel):
    reference_id: str
    timestamp: datetime
    id: str
    fa: str
    name: Optional[str] = None
    phone_number: Optional[str] = None
    additional_info: Optional[List[object]] = None
    locale: Optional[str] = "en"


class UnlinkRequest(BaseModel):
    transaction_id: str
    unlink_request: List[SingleUnlinkRequest]


class SingleUnlinkResponse(BaseModel):
    reference_id: str
    timestamp: datetime
    id: Optional[str] = ""
    status: StatusEnum
    status_reason_code: Optional[UnlinkStatusReasonCode] = None
    status_reason_message: Optional[str] = ""
    additional_info: Optional[List[object]] = None
    locale: Optional[str] = "en"


class UnlinkResponse(BaseModel):
    transaction_id: str
    correlation_id: Optional[str] = ""
    unlink_response: List[SingleUnlinkResponse]
