from controller import httpController


httpController = httpController.HttpController()

response = httpController.get('https://tails1101.cafe24.com/test/signin_get.php',
    {
        'username': 'admin',
        'password': '1111',
    }
)

if response is not None:
    if response['success']:
        print('이름:', response['name'])
    else:
        print('통신 중 오류가 발생하였습니다.')
else:
    print('통신 중 오류가 발생하였습니다.')


response = httpController.post('https://tails1101.cafe24.com/test/signin_post_json.php',
    {
        'username': 'admin',
        'password': '1111',
    }
)

if response is not None:
    if response['success']:
        print('이름:', response['name'])
    else:
        print('통신 중 오류가 발생하였습니다.')
else:
    print('통신 중 오류가 발생하였습니다.')
