from fastapi import APIRouter
import numpy as np

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


@router.get('/multiply_matrices')
async def multiply_matrices():
    matrix_a = np.random.randn(10, 10)
    matrix_b = np.random.randn(10, 10)

    product = np.dot(matrix_a, matrix_b)

    return {
        'matrix_a': matrix_a.tolist(),
        'matrix_b': matrix_b.tolist(),
        'product': product.tolist()
    }
