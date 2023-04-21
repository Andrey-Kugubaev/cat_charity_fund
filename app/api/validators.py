from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charityproject import charity_project_crud
from app.models.charity_project import CharityProject


async def check_info_none(
        object: str,
        session: AsyncSession,
) -> None:
    if object is None:
        raise HTTPException(
            status_code=422,
            detail='Field can not be None'
        )


async def check_name_duplicate(
        charity_project: str,
        session: AsyncSession,
) -> None:
    project_id = await charity_project_crud.get_project_id_by_name(charity_project, session)
    if project_id is not None:
        raise HTTPException(
            status_code=400,
            detail='Проект с таким именем уже существует!'
        )


async def check_charity_project_exists(
        project_id: int,
        session: AsyncSession,
) -> CharityProject:
    charity_project = await charity_project_crud.get(
        object_id=project_id, session=session
    )
    if charity_project is None:
        raise HTTPException(
            status_code=404,
            detail='Charity project is not found'
        )
    return charity_project


async def check_delete_project_invested(
        project_id: int,
        session: AsyncSession,
) -> CharityProject:
    charity_project = await charity_project_crud.get(
        object_id=project_id, session=session
    )
    if charity_project.invested_amount > 0:
        raise HTTPException(
            status_code=400,
            detail='В проект были внесены средства, не подлежит удалению!'
        )
    return charity_project


async def check_delete_project_closed(
        project_id: int,
        session: AsyncSession,
):
    charity_project = await charity_project_crud.get(
        object_id=project_id, session=session
    )
    if charity_project.fully_invested is True:
        raise HTTPException(
            status_code=400,
            detail='В проект были внесены средства, не подлежит удалению!'
        )
    return charity_project


async def check_update_project_closed(
        project_id: int,
        session: AsyncSession,
):
    charity_project = await charity_project_crud.get(
        object_id=project_id, session=session
    )
    if charity_project.fully_invested is True:
        raise HTTPException(
            status_code=400,
            detail='Закрытый проект нельзя редактировать!'
        )
    return charity_project


async def check_update_project_invested(
        project_id: int,
        session: AsyncSession,
):
    charity_project = await charity_project_crud.get(
        object_id=project_id, session=session
    )
    if charity_project.full_amount < charity_project.invested_amount:
        raise HTTPException(
            status_code=422,
            detail='При редактировании проекта должно быть запрещено'
                   'устанавливать требуемую сумму меньше внесённой.'
        )
    return charity_project