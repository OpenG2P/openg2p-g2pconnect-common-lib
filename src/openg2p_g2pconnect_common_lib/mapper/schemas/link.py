from enum import Enum
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

from ...common.schemas import StatusEnum


class SingleLinkRequest(BaseModel):
    reference_id: str
    timestamp: datetime
    id: str
    fa: str
    name: Optional[str] = None
    phone_number: Optional[str] = None
    additional_info: Optional[List[object]] = None
    locale: Optional[str] = "en"


class LinkRequest(BaseModel):
    transaction_id: str
    link_request: List[SingleLinkRequest]


class LinkStatusReasonCode(Enum):
    rjct_reference_id_invalid = "rjct.reference_id.invalid"
    rjct_reference_id_duplicate = "rjct.reference_id.duplicate"
    rjct_timestamp_invalid = "rjct.timestamp.invalid"
    rjct_id_invalid = "rjct.id.invalid"
    rjct_fa_invalid = "rjct.fa.invalid"
    rjct_name_invalid = "rjct.name.invalid"
    rjct_mobile_number_invalid = "rjct.mobile_number.invalid"
    rjct_unknown_retry = "rjct.unknown.retry"
    rjct_other_error = "rjct.other.error"


class SingleLinkResponse(BaseModel):
    reference_id: str
    timestamp: datetime
    fa: Optional[str] = None
    status: StatusEnum
    status_reason_code: Optional[LinkStatusReasonCode] = None
    status_reason_message: Optional[str] = None
    additional_info: Optional[List[object]] = None
    locale: Optional[str] = "en"


class LinkResponse(BaseModel):
    transaction_id: str
    correlation_id: Optional[str] = None
    link_response: List[SingleLinkResponse]
