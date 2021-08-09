from infraestructure.repository.auth import LdapRepository, UserRepository
from starlette.status import HTTP_401_UNAUTHORIZED
from fastapi import HTTPException
from infraestructure.utils import Config
from datetime import datetime, timedelta
import jwt


class AuthService():

    def __init__(self):
        self.ldap = LdapRepository()
        self.repository = UserRepository()
        self.config = Config().get_config(section='jwt')

    def authenticate_user(self, username, password):
        """[summary]
                Autentica el usuario
            Arguments:
                username {str} -- the user name
                password {str} -- the user password

            Raises:
                Exception -- [description]
        """
        credentials_exception = HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        response = {"access_token": None, "user": None, "token_type": "bearer"}
        valid_user = self.ldap.validate_identity(str(username), str(password))
        if valid_user:
            user = self.repository.get_user_by_name(username)
            if user is None:
                user_info = self.ldap.get_login_info(username, password)
                self.repository.create_user(str(username), str(
                    user_info.displayName), str(user_info.mail))
                user = self.repository.get_user_by_name(username)
            response['access_token'] = self.__create_access_token(
                {"user_id": user['UserId']})
            response['user'] = user
            return response
        else:
            raise credentials_exception

    def get_modules(self, userid):
        return self.repository.get_modules(userid)

    def __create_access_token(self, data: dict):

        to_encode = data.copy()
        expire = datetime.utcnow() + \
            timedelta(days=int(self.config['expire_time']))

        to_encode.update(
            {"exp": expire, "sub": self.config['access_token_subject']})

        encoded_jwt = jwt.encode(
            to_encode, self.config['secret_key'], algorithm=self.config['algorithm'])
        return encoded_jwt
