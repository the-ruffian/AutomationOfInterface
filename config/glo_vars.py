"""
    @Author: TheRuffian
    @Email: bugpz2779@gmail.com
    @CSDN: 'https://blog.csdn.net/BUGPZ'
    @StackOverFlow: 'https://stackoverflow.com/users/12850648/theruffian'
"""

from common.document_operation import read_yaml


def url_glo():
    return f"{read_yaml('../config/env.yaml')['env']['url']}"
