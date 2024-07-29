import uvicorn


if __name__ == '__main__':
    check = 'start'
    if check == 'start':
        check = 'run'
        uvicorn.run('page:app', port=8080, workers=2, lifespan='on')
