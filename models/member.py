# coding: utf-8
import leancloud

class Member(leancloud.Object):
  @staticmethod
  def update_member(data = None, **kv):
    if data == None: data = {}
    data.update(kv)
    user = Member()
    if data['id'] != "":
      user = Member.create_without_data(data['id'])
      user.fetch()
      if data.has_key('status'): user.set('status', data['status'])
      if data.has_key('avatar_id') and user.get('avatar_id') != data['avatar_id']:
        f = leancloud.File.create_without_data(user.get('avatar_id'))
        f.destroy()
    else:
      user.set('status', 0)
    if data.has_key('phone'): user.set('phone', data['phone'])
    if data.has_key('email'): user.set('email', data['email'])
    if data.has_key('name'): user.set('name', data['name'])
    if data.has_key('gender'): user.set('gender', data['gender'])
    if data.has_key('dob'): user.set('dob', data['dob'])
    if data.has_key('avatar'): user.set('avatar', data['avatar'])
    if data.has_key('avatar_id'): user.set('avatar_id', data['avatar_id'])
    if data.has_key('signature'): user.set('signature', data['signature'])
    if data.has_key('description'): user.set('description', data['description'])
    user.save()

  @staticmethod
  def fetch_members(**data):
    ls = Member.query.add_descending('createdAt').skip(data['rows'] * data['page']).limit(data['rows']).find()
    res = []
    for i in ls:
      res.append({
        'id': i.id,
        'phone': i.get('phone'),
        'email': i.get('email'),
        'name': i.get('name'),
        'gender': i.get('gender'),
        'dob': i.get('dob'),
        'avatar_id': i.get('avatar_id'),
        'avatar': i.get('avatar'),
        'signature': i.get('signature'),
        'description': i.get('description'),
        'status': i.get('status')
      })
    return res
