from typing import List, Optional

from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from starlette import status

from ..database import get_session
from ..models.clients import ClientBase, Client
from .. import tables

router = APIRouter(
    prefix='/users'
)


@router.get('/all', response_model=List[Client])
def get_client_list(session: Session = Depends(get_session)):
    query = session.query(tables.Clients)
    clients = query.all()
    return clients


@router.get('/{id}', response_model=Client)
def get_client_by_id(id: int, session: Session = Depends(get_session)):
    query = session.query(tables.Clients)
    client = query.get(id)
    return client


@router.post('/', response_model=Client)
def create_client(client_data: ClientBase, session: Session = Depends(get_session)):
    client = tables.Clients(**client_data.dict())
    session.add(client)
    session.commit()
    return client


@router.put('/{id}', response_model=Client)
def update_client_data(id: int, client_data: ClientBase, session: Session = Depends(get_session)):
    query = session.query(tables.Clients)
    client = query.get(id)
    for field, value in client_data:
        setattr(client, field, value)
    session.commit()
    return client


@router.delete('/{id}', response_model=Client)
def delete_client(id: int, session: Session = Depends(get_session)):
    query = session.query(tables.Clients)
    client = query.get(id)
    session.delete(client)
    session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
