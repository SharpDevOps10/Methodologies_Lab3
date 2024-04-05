from fastapi import APIRouter

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {
        'first_name': 'Danyil',
        'last_name': 'Tymofeiev',
        'age': 18,
        'group_code': 'IM-22'
    }
