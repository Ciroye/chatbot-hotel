from fastapi import APIRouter, Body, Depends, HTTPException
from infraestructure.utils.auth import get_current_user
from domain.services.agent import AgentService
from domain.models.agent import RequestModel, ResponseModel
from typing import List
import redis

router = APIRouter()


@router.post('/chat', response_model=ResponseModel)
def get_permissions(u: RequestModel):
    return AgentService(1).init_web_conversation(u)
