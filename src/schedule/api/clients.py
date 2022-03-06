from typing import List

from fastapi import APIRouter

from ..database import Session
from ..models.clients import Client
from .. import tables

router = APIRouter(
    prefix='/users'
)


@router.get('/all', response_model=List[Client])
def get_client_list():
    session = Session()
    clients = (
        session
        .query(tables.Clients)
        .all()
    )
    return clients


@router.get('/{id}')
def get_user_by_id():
    return {"message": id}