import requests


def get_auth_url():
    weibo_auth_url = "https://api.weibo.com/oauth2/authorize"
    redirect_uri = "http://47.92.87.172:8000/complete/weibo/"
    # redirect_uri = "http://127.0.0.1:8088/complete/weibo/"
    auth_url = weibo_auth_url+"?client_id={client_id}&redirect_uri={re_url}".format(
        client_id=272636935, re_url=redirect_uri)
    print(auth_url)


def get_access_token(code="406764c515abfa84f92bf9de8e0e715f"):
    access_token_url = "https://api.weibo.com/oauth2/access_token"
    re_dict = requests.post(access_token_url, data={
        "client_id": 272636935,
        "client_secret": "915387c62b9167c39edd7402e07e0cf0",
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": "http://47.92.87.172:8000/complete/weibo/"
    })

    print(re_dict.text)


def get_user_info(access_token="", uid=""):
    user_url = "https://api.weibo.com/2/friendships/friends.json?access_token={token}&uid={uid}".format(
        token=access_token, uid=uid)
    print(user_url)


def get_user_info_name(access_token="", screen_name=""):
    user_url = "https://api.weibo.com/2/friendships/friends.json?access_token={token}&screen_name={screen_name}".format(
        token=access_token, screen_name=screen_name)
    print(user_url)


if __name__ == '__main__':
    get_auth_url()
    get_access_token(code="406764c515abfa84f92bf9de8e0e715f")

    get_user_info(access_token="2.00LMmr1E0v_x8S83cc8cf309anmHjC", uid="3972874699")
    # get_user_info_name(access_token="2.00LMmr1E0v_x8S83cc8cf309anmHjC", screen_name="生活总是未知的_741")
