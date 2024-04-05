from fastapi import APIRouter

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {
        'first_name': 'Danyil',
        'last_name': 'Tymofeiev',
        'age': 18,
        'group_code': 'IM-22',
        'email': 'london@capital.org',
        'date_of_birth': '2023-09-05 06:25:00.000',
        'pronouns': 'wee/woo'
    }
