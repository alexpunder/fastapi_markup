from multiprocessing import freeze_support

import uvicorn


if __name__ == '__main__':
    freeze_support()
    uvicorn.run('page:app', port=8080, workers=4)
