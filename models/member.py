# coding: utf-8
import leancloud

class Member(leancloud.Object):
  @staticmethod
  def create_member(**data):
    user = Member()
    user.set('name', data['name'])
    user.set('gender', data['gender'])
    user.set('dob', data['dob'])
    user.set('avatar', data['avatar'])
    user.set('signature', data['signature'])
    user.set('description', data['description'])
    user.set('status', 0)
    user.save()

  @staticmethod
  def fetch_members(**data):
    ls = Member.query.equal_to('status', 0).skip(data['rows'] * data['page']).limit(data['rows']).find()
    res = []
    for i in ls:
      res.append({
        'id': i.id,
        'name': i.get('name'),
        'gender': i.get('gender'),
        'dob': i.get('dob'),
        'avatar': i.get('avatar'),
        'signature': i.get('signature'),
        'description': i.get('description'),
        'status': i.get('status')
      })
    return res