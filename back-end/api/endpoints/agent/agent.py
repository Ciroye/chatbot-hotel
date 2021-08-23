from fastapi import APIRouter

from domain.models.agent import RequestModel, ResponseModel
from domain.services.agent import AgentService

router = APIRouter()


@router.post('/chat', response_model=ResponseModel)
def get_permissions(u: RequestModel):
    return AgentService().init_web_conversation(u)
