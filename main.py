import time

import itchat
from itchat.content import TEXT, MAP, CARD, NOTE, SHARING, PICTURE, RECORDING, ATTACHMENT, VIDEO, FRIENDS


# 接受文本信息
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING], isFriendChat=True)
def accept_friend_chat(msg):

    print(msg.text, msg.ToUserName, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg.CreateTime)))
    # msg.user.send('%s: %s' % (msg.type, msg.text))


#
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING], isMpChat=True)
def accept_mp_chat(msg):
    print(msg.User.NickName, msg.text, msg.ToUserName, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg.CreateTime)))
    # if msg.isAt:
    #     print(msg)
    # msg.user.send(u'@%s\u2005I received: %s' % (
    #     msg.actualNickName, msg.text))


# 群消息
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING], isGroupChat=True)
def accept_group_chat(msg):
    print(msg.User.NickName, msg.text, msg.ToUserName, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg.CreateTime)))
    # if msg.isAt:
    #     print(msg)
    # msg.user.send(u'@%s\u2005I received: %s' % (
    #     msg.actualNickName, msg.text))


# 下载文件
@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg.download(msg.fileName)
    print(msg.fileName)
    typeSymbol = {
        PICTURE: 'img',
        VIDEO: 'vid', }.get(msg.type, 'fil')
    return '@%s@%s' % (typeSymbol, msg.fileName)


# 自动添加好友
@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    print(msg.user)
    msg.user.send('Nice to meet you!')


if __name__ == '__main__':
    itchat.auto_login(True)
    itchat.run(True)
