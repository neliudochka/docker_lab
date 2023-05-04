from fastapi import APIRouter

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {'msg': 'Hello, World!'}

@router.get('/product')
def matrix_product() -> dict:
    import numpy as np

    matrix1 = np.random.rand(10, 10)
    matrix2 = np.random.rand(10, 10)

    res = np.dot(matrix1, matrix2)

    return {
        'matrix1': matrix1.tolist(), 
        'matrix2': matrix2.tolist(), 
        'product': res.tolist()
    }