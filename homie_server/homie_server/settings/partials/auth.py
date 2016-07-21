import os

# AUTH
AUTH_USER_MODEL = "users.User"

# LOGIN_URL = "/login/"
# LOGIN_URL = "/api-token-auth/"

SIGNUP_SUCCESS_MESSAGE = "성공적으로 회원가입 되었습니다."
LOGIN_SUCCESS_MESSAGE = "성공적으로 로그인 되었습니다."
LOGOUT_SUCCESS_MESSAGE = "성공적으로 로그아웃 되었습니다."

AUTHENTICATION_BACKENDS = [
    "social.backends.facebook.FacebookOAuth2",
    "social.backends.kakao.KakaoOAuth2",

    "django.contrib.auth.backends.ModelBackend",
]

SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get("SOCAIAL_AUTH_FACEBOOK_KEY")
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get("SOCAIAL_AUTH_FACEBOOK_KEY")

SOCIAL_AUTH_KAKAO_KEY = os.environ.get("SOCIAL_AUTH_KAKAO_KEY")
SOCIAL_AUTH_KAKAO_SECRET = os.environ.get("SOCIAL_AUTH_KAKAO_SECRET")

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
)

SOCIAL_AUTH_LOGIN_REDIRECT_URL = "/"
SOCIAL_AUTH_LOGIN_ERROR_URL = "/"
SOCIAL_AUTH_LOGIN_URL = "/"
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = "/login/"
