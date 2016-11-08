# coding: utf-8
import leancloud

class User(leancloud.Object):
  def createUser(**data):
    user = User()
    user.set('name', data['name'])
    user.set('gender', data['gender'])
    user.set('dob', data['dob'])
    user.set('avatar', data['avatar'])
    user.set('signature', data['signature'])
    user.set('description', data['description'])
    user.set('status', 0)
    user.save()