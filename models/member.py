# coding: utf-8
import leancloud

class Member(leancloud.Object):
  @staticmethod
  def update_member(**data):
    print data
    user = Member()
    if data['id'] != "":
      user = Member.create_without_data(data['id'])
      user.set('status', data['status'])
    else:
      user.set('status', 0)
    user.set('phone', data['phone'])
    user.set('email', data['email'])
    user.set('name', data['name'])
    user.set('gender', data['gender'])
    user.set('dob', data['dob'])
    user.set('avatar', data['avatar'])
    user.set('signature', data['signature'])
    user.set('description', data['description'])
    user.save()

  @staticmethod
  def fetch_members(**data):
    ls = Member.query.skip(data['rows'] * data['page']).limit(data['rows']).find()
    res = []
    for i in ls:
      res.append({
        'id': i.id,
        'phone': i.get('phone'),
        'email': i.get('email'),
        'name': i.get('name'),
        'gender': i.get('gender'),
        'dob': i.get('dob'),
        'avatar': i.get('avatar'),
        'signature': i.get('signature'),
        'description': i.get('description'),
        'status': i.get('status')
      })
    return res
